from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        
    def __str__(self):
            return f'warehouse {self.name}'