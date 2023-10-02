from warehouses.models import Warehouse
from .serializers import WarehouseSerializer
from rest_framework.viewsets import ModelViewSet


class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer