from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.ListCustomer, name='customer-list'),
    path('customers/<uuid:pk>/', views.DetailCustomer, name='customer-detail'),
    path('products/', views.ProductList, name='product-list'),
    path('products/<uuid:pk>/', views.ProductDetail, name='product-detail'),
]