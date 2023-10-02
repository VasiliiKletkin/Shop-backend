from carts.models import Cart
from rest_framework.viewsets import ModelViewSet

from .serializers import CartSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer