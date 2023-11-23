from rest_framework import serializers

from .models import Product, ProductItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    total_price = serializers.ReadOnlyField()
    class Meta:
        model = ProductItem
        fields = '__all__'
