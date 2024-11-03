from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('prod/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path('prod/create/', ProductCreateView.as_view(), name='products_create'),
    path('prod/<int:pk>/update/', ProductUpdateView.as_view(), name='products_update'),
    path('prod/<int:pk>/delete/', ProductDeleteView.as_view(), name='products_delete'),
]