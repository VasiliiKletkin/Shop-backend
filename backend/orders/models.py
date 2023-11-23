from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from model_utils import Choices
from model_utils.fields import MonitorField, StatusField
from products.models import ProductItem

User = get_user_model()


class Order(models.Model):
    ORDER_STATUS_CONFIRMATION = "CONFIRMATION"
    ORDER_STATUS_COMPLETED = "COMPLETED"
    ORDER_STATUS_CANCELED = "CANCELED"
    ORDER_STATUS_CHOICES = Choices(
        (ORDER_STATUS_CONFIRMATION, 'Подтверждение'),
        (ORDER_STATUS_COMPLETED, 'Выполнен'),
        (ORDER_STATUS_CANCELED, 'Отменен'),
    )
    status = StatusField(
        "Статус заказа", choices_name="ORDER_STATUS_CHOICES", default=ORDER_STATUS_CONFIRMATION)

    PAYMENT_ONLINE_TRANSFER = "ONLINE_TRANSFER"
    PAYMENT_TYPES = Choices(
        (PAYMENT_ONLINE_TRANSFER, "Онлайн перевод"),
    )
    payment_type = models.CharField(
        "Тип оплаты", choices=PAYMENT_TYPES, max_length=30, default=PAYMENT_ONLINE_TRANSFER)

    # created_date = models.DateTimeField(auto_now_add=True)
    completed_date = MonitorField(
        "Дата выполнения заказа", monitor="status", when=[ORDER_STATUS_COMPLETED], null=True, blank=True)
    canceled_date = MonitorField(
        "Дата отмены заказа", monitor="status", when=[ORDER_STATUS_CANCELED], null=True, blank=True)

    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="orders")
    product_items = GenericRelation(ProductItem, related_query_name="order")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"order {self.id}"

    # @property
    def total_price(self):
        return sum(item.total_price() for item in self.product_items.all())
