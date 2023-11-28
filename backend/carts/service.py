from decimal import Decimal

from django.conf import settings
from products.models import Product
from django.forms.models import model_to_dict
from django.core.cache import cache

class Cart:
    def __init__(self, request):
        """
        initialize the cart
        """
        self.user_id = request.user.id
        self.cart = cache.get(f"{settings.CART_SESSION_ID}_{self.user_id}", {})
        self.cart_items = self.__iter__()
        self.total_price = self.get_total_price()

    def save(self):
        self.cart = cache.set(f"{settings.CART_SESSION_ID}_{self.user_id}", self.cart)

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

    def clear(self):
        self.cart = {}
        self.save()