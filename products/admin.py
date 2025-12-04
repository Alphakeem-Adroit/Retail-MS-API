# Register your models here.
# admin.py
from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # number of blank image fields
    # fields = ['image']  # optional

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
