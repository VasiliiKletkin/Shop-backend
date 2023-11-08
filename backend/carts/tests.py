# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.status import HTTP_200_OK

# from .models import Cart


# class CartViewSetTestCase(TestCase):
#     def setUp(self):
#         User = get_user_model()
#         self.user = User.objects.create(username="test", password="test")
        
#     def test_get_carts(self):
#         response = self.client.get(reverse("internal_api:carts_api:cart-list"))
#         self.assertEqual(response.status_code, HTTP_200_OK)
#         self.assertEqual(response.data, [])
        
#     def test_get_carts_with_items(self):
#         Cart.objects.create(user=self.user)
#         response = self.client.get(reverse("internal_api:carts_api:cart-list"))
#         self.assertEqual(response.status_code, HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
        