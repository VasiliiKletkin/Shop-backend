from rest_framework.viewsets import ModelViewSet

from .models import Product, ProductItem
from .serializers import ProductItemSerializer, ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductItemViewSet(ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
