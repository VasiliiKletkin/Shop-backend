from products.models import Product, ProductItem
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = '__all__'
