from products.models import Product
from rest_framework.viewsets import ModelViewSet

from .serializers import ProductItemSerializer, ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductItemViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductItemSerializer
    