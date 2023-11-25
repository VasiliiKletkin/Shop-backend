from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return f'category {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/products')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'product {self.name}'


class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return f'PLI {self.product} {self.quantity}'

    # @property
    def total_price(self):
        return self.quantity * self.product.price


class ProductItemMixin(models.Model):
    product_items = GenericRelation(
        ProductItem)

    class Meta:
        abstract = True
        
    def update_or_create(self, product_id, quantity):
        obj, created = self.product_items.update_or_create(
            product_id=product_id, defaults={'quantity': quantity})
        return obj

    def delete(self, product_id):
        self.product_items.filter(product_id=product_id).delete()

    def total_price(self):
        return sum(item.total_price() for item in self.product_items.all())
