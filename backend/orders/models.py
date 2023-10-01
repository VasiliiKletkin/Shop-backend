from django.contrib.auth import get_user_model
from django.db import models
from model_utils.models import TimeStampedModel

User = get_user_model()


class Order(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orders")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"order {self.id}"
