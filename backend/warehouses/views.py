from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Warehouse
from .serializers import WarehouseSerializer


class WarehouseViewSet(ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    serializer_detail_class = WarehouseSerializer
    
    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.serializer_detail_class
        return super().get_serializer_class()
    