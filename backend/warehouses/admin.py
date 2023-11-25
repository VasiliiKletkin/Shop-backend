from django.contrib import admin
from products.admin import ProductItemInline

from .models import Warehouse


class WarehouseAdmin(admin.ModelAdmin):
    inlines = [ProductItemInline]


admin.site.register(Warehouse, WarehouseAdmin)
