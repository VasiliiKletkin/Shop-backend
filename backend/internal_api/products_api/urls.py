from django.urls import include, path
from rest_framework import routers

from .views import ProductItemViewSet, ProductViewSet

app_name = 'products_api'

router = routers.DefaultRouter()
router.register('', ProductViewSet)
router.register('product_items', ProductItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
