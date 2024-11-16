from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductUnpublishView, ProductByCategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('prod/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='products_detail'),
    path('prod/create/', ProductCreateView.as_view(), name='products_create'),
    path('prod/<int:pk>/update/', ProductUpdateView.as_view(), name='products_update'),
    path('prod/<int:pk>/delete/', ProductDeleteView.as_view(), name='products_delete'),
    path('prod/<int:pk>/unpublish/', ProductUnpublishView.as_view(), name='products_unpublish'),
    path('prod/category/', ProductByCategoryListView.as_view(), name='product_by_category_list')
]