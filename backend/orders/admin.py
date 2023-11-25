from django.contrib import admin
from orders.models import Order, OrderItem
from django.contrib.admin import TabularInline


class ProductItemInline(TabularInline):
    model = OrderItem
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductItemInline]
    list_display = ('id', 'status', 'payment_type', 'total_price')


admin.site.register(Order, OrderAdmin)
