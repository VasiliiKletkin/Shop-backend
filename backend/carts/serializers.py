from rest_framework import serializers
from products.serializers import ProductItemSerializer
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    product_items = ProductItemSerializer(many=True)
    total_price = serializers.ReadOnlyField()
    class Meta:
        model = Cart
        fields = '__all__'
