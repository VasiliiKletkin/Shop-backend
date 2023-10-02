from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from model_utils.models import TimeStampedModel
from products.models import ProductItem

User = get_user_model()


class Order(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orders")
    product_items = GenericRelation(ProductItem, related_query_name="cart")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"order {self.id}"
    
    def total_price(self):
        return sum(item.total_price() for item in self.product_items.all())
