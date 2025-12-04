# from django.shortcuts import render

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# List all products with images
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

# Retrieve a single product with images
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
