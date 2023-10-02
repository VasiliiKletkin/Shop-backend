from products.models import Product
from .serializers import ProductItemSerializer, ProductSerializer
from rest_framework.viewsets import ModelViewSet


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductItemViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductItemSerializer
    
class ProductItemViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductItemSerializer