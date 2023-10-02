from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from products.models import ProductItem


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    product_items = GenericRelation(ProductItem, related_query_name="warehouse")
    
    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        
    def __str__(self):
            return f'warehouse {self.name}'