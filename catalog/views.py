from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(
            f"{name}, указанные Вами телефон и сообщение получены<br>Телефон: {phone}<br>Сообщение: {message}"
        )
    return render(request, "contacts_content.html")

def products_detail(request, pk):
    products = Product.objects.get(pk=pk)
    context = {'products': products}
    return render(request, 'products_detail.html', context)
