# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.status import HTTP_200_OK

# from .models import Order


# class OrderViewSetTestCase(TestCase):
#     def setUp(self):
#         User = get_user_model()
#         self.user = User.objects.create(username="test", password="test")
        
#     def test_get_orders(self):
#         response = self.client.get(reverse("internal_api:orders_api:order-list"))
#         self.assertEqual(response.status_code, HTTP_200_OK)
#         self.assertEqual(response.data, [])
        
#     def test_get_orders_with_items(self):
#         Order.objects.create(user=self.user)
#         response = self.client.get(reverse("internal_api:orders_api:order-list"))
#         self.assertEqual(response.status_code, HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
        