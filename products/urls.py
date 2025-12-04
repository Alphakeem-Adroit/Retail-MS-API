from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    # Products
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
