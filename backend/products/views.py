from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductItemSerializer, ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductItemViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductItemSerializer
