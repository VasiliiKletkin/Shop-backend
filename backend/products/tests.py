# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.status import HTTP_200_OK

# from .models import Product


# class ProductApiTestCase(TestCase):
#     def test_get_products(self):
#         response = self.client.get(reverse("internal_api:products_api:product-list"))
#         self.assertEqual(response.status_code, HTTP_200_OK)
#         self.assertEqual(response.data, [])
    
#     def test_get_product_with_items(self):
#         Product.objects.create(name="test", price=100, description="test", image="test")
#         response = self.client.get(reverse("internal_api:products_api:product-list"))
#         self.assertEqual(response.status_code, HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
