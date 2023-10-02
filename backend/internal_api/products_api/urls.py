from rest_framework import routers
from django.urls import path, include

from .views import ProductViewSet


app_name = 'products_api'

router = routers.DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
