from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from products.models import ProductItem
from carts.models import Cart
from carts.serializers import CartSerializer
from products.serializers import ProductItemSerializer


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
