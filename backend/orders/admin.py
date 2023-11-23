from django.contrib import admin
from orders.models import Order
from products.models import ProductItem
from django.contrib.contenttypes.admin import GenericTabularInline


class ProductItemInline(GenericTabularInline):
    model = ProductItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductItemInline]


admin.site.register(Order, OrderAdmin)
