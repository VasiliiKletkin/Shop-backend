from decimal import Decimal

from django.conf import settings
from products.models import Product
from coupons.models import Coupon
from django.core.cache import cache
from rest_framework.exceptions import NotAuthenticated


class Cart:
    def __init__(self, request):
        """
        initialize the cart
        """
        if request.user.is_anonymous:
            raise NotAuthenticated("User is not authenticated")
        self.user_id = request.user.id
        self.coupon_code = request.query_params.get('coupon', None)
        self.cart = cache.get(f"{settings.CART_SESSION_ID}_{self.user_id}", {})
        self.items = self.__iter__()
        self.total_price = self.get_total_price()
        self.total_price_after_discount = self.get_total_price_after_discount()
        self.discount = self.get_discount()

    def save(self):
        self.cart = cache.set(
            key=f"{settings.CART_SESSION_ID}_{self.user_id}", value=self.cart, timeout=15552000)

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add product to the cart or update its quantity
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
            }
        if update_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def remove(self, product):
        """
        Remove a product from the cart
        """
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.cart = {}
        self.save()

    def __iter__(self):
        """
        Loop through cart items and fetch the products from the database
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]["product"] = product
        for item in cart.values():
            item["total_price"] = item["product"].price * item["quantity"]
            yield item

    def __len__(self):
        """
        Count all items in the cart
        """
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return sum(product.price * self.cart[str(product.id)]["quantity"] for product in products)

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) * self.get_total_price()
        return 0

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()

    @property
    def coupon(self):
        return Coupon.objects.get(code=self.coupon_code) if self.coupon_code else None
