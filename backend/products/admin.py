from django.contrib import admin

from .models import Product, ProductItem


class ProductAdmin(admin.ModelAdmin):
    pass


class ProductItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductItem, ProductAdmin)
