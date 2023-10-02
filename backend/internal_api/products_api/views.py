from products.models import Product
from .serializer import ProductSerializer, ProductItemSerializer
from rest_framework.viewsets import ModelViewSet


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductItemViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductItemSerializer