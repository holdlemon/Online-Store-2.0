from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.products, name='products'),
    path('contacts/', views.contacts, name='contacts'),
    path('prod/<int:pk>/', views.products_detail, name='products_detail'),
]