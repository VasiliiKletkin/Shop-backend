from products.serializers import ProductItemSerializer
from rest_framework import serializers

from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    payment_type_display = serializers.CharField(
        source="get_payment_type_display")
    status_display = serializers.CharField(
        source="get_status_display")
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderDetailSerializer(OrderSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
