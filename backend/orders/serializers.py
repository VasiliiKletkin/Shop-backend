from rest_framework import serializers
from products.serializers import ProductItemSerializer

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()
    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()
    product_items = ProductItemSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'