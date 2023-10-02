from rest_framework import routers
from django.urls import path, include

from .views import WarehouseViewSet


app_name = 'warehouses_api'

router = routers.DefaultRouter()
router.register('', WarehouseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
