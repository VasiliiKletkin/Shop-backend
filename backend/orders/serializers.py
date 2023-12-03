from rest_framework import serializers

from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    payment_type_display = serializers.ReadOnlyField(
        source='get_payment_type_display')
    status_display = serializers.ReadOnlyField(
        source='get_payment_type_display')
    total_price = serializers.ReadOnlyField(
        source='get_total_price')

    class Meta:
        model = Order
        exclude = ['user',]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class OrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField(source='get_total_price')

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderDetailSerializer(OrderSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta(OrderSerializer.Meta):
        model = Order
        fields = '__all__'
