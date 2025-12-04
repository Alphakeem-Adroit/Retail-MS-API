from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer

# List all products
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

# Retrieve a single product
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Optional: List all product images
class ProductImageListView(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

# Optional: Get images for a single product
class ProductImagesByProductView(generics.ListAPIView):
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        product_id = self.kwargs['pk']
        return ProductImage.objects.filter(product_id=product_id)
