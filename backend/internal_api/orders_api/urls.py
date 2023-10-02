from django.urls import include, path
from rest_framework import routers

from .views import OrderViewSet

app_name = "orders_api"

router = routers.DefaultRouter()
router.register("", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
