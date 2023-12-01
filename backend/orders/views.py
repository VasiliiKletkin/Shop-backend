from orders.models import Order, OrderItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from carts.service import Cart
from rest_framework import status

from .serializers import OrderSerializer, OrderDetailSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    serializer_detail_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.serializer_detail_class
        return super().get_serializer_class()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        cart = Cart(request)
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['product'].price,
                                     quantity=item['quantity'])
        cart.clear()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
