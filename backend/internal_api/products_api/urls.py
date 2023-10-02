from rest_framework import routers
from django.urls import path, include

from .views import ProductViewSet, ProductItemViewSet


app_name = 'products_api'

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('product_items', ProductItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
