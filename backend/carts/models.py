from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from .models import ProductItem

User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="cart")
    product_items = GenericRelation(ProductItem, related_query_name="cart")

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"cart {self.user}"
