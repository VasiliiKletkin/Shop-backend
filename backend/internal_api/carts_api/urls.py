from django.urls import include, path
from rest_framework import routers

from .views import CartViewSet

app_name = "carts_api"

router = routers.DefaultRouter()
router.register("", CartViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
