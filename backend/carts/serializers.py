from rest_framework import serializers

from products.models import Product
from products.serializers import ProductSerializer

class CartItemWriteSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField(min_value=1)
    total_price = serializers.ReadOnlyField()
    

class CartItemReadSerializer(serializers.Serializer):
    product = ProductSerializer()
    quantity = serializers.IntegerField(min_value=1)
    total_price = serializers.ReadOnlyField()
    

class CartSerializer(serializers.Serializer):
    items = CartItemReadSerializer(many=True)
    total_price = serializers.ReadOnlyField()
    