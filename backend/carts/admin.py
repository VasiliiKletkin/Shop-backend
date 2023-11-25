from django.contrib import admin
from products.admin import ProductItemInline

from .models import Cart


class CartAdmin(admin.ModelAdmin):
    inlines = [ProductItemInline]


admin.site.register(Cart, CartAdmin)
