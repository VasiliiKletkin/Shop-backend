from django.contrib import admin

from .models import Warehouse


class WarehouseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Warehouse, WarehouseAdmin)
