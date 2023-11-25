from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from products.models import ProductItem, ProductItemMixin

User = get_user_model()


class Cart(ProductItemMixin, models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="cart")

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"cart {self.user}"
