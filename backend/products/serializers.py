from rest_framework import serializers

from .models import Product, ProductItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Product.objects.all())
    total_price = serializers.ReadOnlyField()
    class Meta:
        model = ProductItem
        fields = '__all__'
        fields = ['id','total_price', 'quantity', 'product', 'product_id']
        read_only_fields = ['id','total_price', 'content_type', 'object_id']
