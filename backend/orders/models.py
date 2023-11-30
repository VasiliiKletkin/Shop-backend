from decimal import Decimal

from coupons.models import Coupon
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from model_utils import Choices
from model_utils.fields import MonitorField, StatusField
from products.models import Product

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
    paid = models.BooleanField(default=False)

    coupon = models.ForeignKey(
        Coupon, on_delete=models.PROTECT, related_name='orders', null=True, blank=True)
    discount = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)

    created_date = models.DateTimeField(
        "Дата создания заказа", auto_now_add=True)
    updated_date = models.DateTimeField(
        "Дата последнего обновления", auto_now=True)
    completed_date = MonitorField(
        "Дата выполнения заказа", monitor="status", when=[ORDER_STATUS_COMPLETED], null=True, blank=True)
    canceled_date = MonitorField(
        "Дата отмены заказа", monitor="status", when=[ORDER_STATUS_CANCELED], null=True, blank=True)

    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="orders")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"order {self.id}"

    # @property
    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="order_items")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.price
