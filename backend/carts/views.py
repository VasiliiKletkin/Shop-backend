from carts.models import Cart
from carts.serializers import CartSerializer
from products.models import ProductItem
from products.serializers import ProductItemSerializer
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet


class CartViewSet(GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_object(self):
        return self.get_queryset().first()

    @action(detail=False, methods=['get', 'post', 'delete'], permission_classes=[IsAuthenticated])
    def my(self, request):
        if request.method == 'GET':
            content_object = self.get_object()
            serializer = self.get_serializer(content_object)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            content_object = self.get_object()
            serializer = ProductItemSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            content_object.update_or_create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            content_object = self.get_object()
            serializer = ProductItemSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            content_object.delete(serializer.instance.product_id)
            return Response(serializer.data, status=status.HTTP_200_OK)


# class CartProductItemViewSet(ModelViewSet):
#     queryset = ProductItem.objects.all()
#     serializer_class = ProductItemSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return self.request.user.cart.product_items.all()

#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
        
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

