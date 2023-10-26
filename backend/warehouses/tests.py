from django.test import TestCase
from rest_framework.status import HTTP_200_OK
from .models import Warehouse
from django.urls import reverse



class WarehouseApiTestCase(TestCase):
    def test_get_warehouses(self):
        response = self.client.get(reverse("internal_api:warehouses_api:warehouse-list"))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, [])
    
    def test_get_warehouse_with_items(self):
        Warehouse.objects.create(name="test",)
        response = self.client.get(reverse("internal_api:warehouses_api:warehouse-list"))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
