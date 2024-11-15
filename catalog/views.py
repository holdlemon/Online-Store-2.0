from gc import get_objects
from itertools import product
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView, View

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        prod = form.save()
        user = self.request.user
        prod.owner = user
        prod.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def dispatch(self, request, *args, **kwargs):
        # Получаем объект продукта
        product = super().get_object()
        # Проверяем, является ли текущий пользователь владельцем продукта
        if product.owner == self.request.user:
            return super().dispatch(request, *args, **kwargs)

        return HttpResponseForbidden("Вы не можете изменить этот продукт.")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")

    def dispatch(self, request, *args, **kwargs):
        # Получаем объект продукта
        product = super().get_object()
        # Проверяем, является ли текущий пользователь владельцем продукта
        if product.owner == self.request.user or request.user.has_perm(
            "catalog.delete_product"
        ):
            return super().dispatch(request, *args, **kwargs)

        return HttpResponseForbidden("Вы не можете удалить этот продукт.")




class ProductUnpublishView(LoginRequiredMixin, View):

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden('У вас нет прав для снятия продуктов с публикации')
        product.is_published = False
        product.save()
        return redirect('catalog:products_list')


class ContactsView(LoginRequiredMixin, TemplateView):
    template_name = "catalog/contacts_content.html"

    @staticmethod
    def post(request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"{name}, указанные Вами телефон и сообщение получены<br>Телефон: {phone}<br>Сообщение: {message}"
        )
