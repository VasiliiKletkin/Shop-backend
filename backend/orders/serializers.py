from rest_framework import serializers

from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    payment_type_display = serializers.ReadOnlyField(
        source='get_payment_type_display')
    status_display = serializers.ReadOnlyField(
        source='get_payment_type_display')
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ("payment_type_display",
                  "status_display",
                  "total_price",
                  "first_name",
                  "last_name",
                  "email",
                  "address",
                  "city",)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class OrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderDetailSerializer(OrderSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
