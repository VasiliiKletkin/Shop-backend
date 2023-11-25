from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Product, ProductItem


class ProductAdmin(admin.ModelAdmin):
    pass


class ProductItemAdmin(admin.ModelAdmin):
    pass


class ProductItemInline(GenericTabularInline):
    model = ProductItem


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductItem, ProductAdmin)
