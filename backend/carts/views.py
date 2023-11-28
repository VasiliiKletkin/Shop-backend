from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from .serializers import CartSerializer, CartItemWriteSerializer, CartItemReadSerializer
from django.forms.models import model_to_dict

from .service import Cart


class CartAPI(APIView):
    """
    Single API to handle cart operations
    """

    def get(self, request, format=None):
        cart = Cart(request)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        cart = Cart(request)
        if "clear" in request.data:
            cart.clear()
            return Response({"message": "Cart cleared"},status=status.HTTP_204_NO_CONTENT)
        serializer = CartItemWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart.remove(product=model_to_dict(serializer.validated_data["product"]))
        return Response({"message": "Removed from cart"}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request, **kwargs):
        cart = Cart(request)
        serializer = CartItemWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart.add(
            product=model_to_dict(serializer.validated_data["product"]),
            quantity=serializer.validated_data["quantity"],
            override_quantity=bool(
                request.data.get("override_quantity", False)),
        )
        return Response({"message": "Added to cart"}, status=status.HTTP_202_ACCEPTED)
