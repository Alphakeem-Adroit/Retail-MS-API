# from django.urls import path
# from .views import ProductListView, ProductDetailView

# urlpatterns = [
#     # Products
#     path('products/', ProductListView.as_view(), name='product-list'),
#     path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
# router.register(r'product-images', ProductImageViewSet, basename='product-image')

urlpatterns = [
    path('', include(router.urls)),
]
