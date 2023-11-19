from carts.views import CartViewSet
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from orders.views import OrderViewSet
from products.views import ProductItemViewSet, ProductViewSet
from rest_framework import routers
from warehouses.views import WarehouseViewSet
from users.views import UserViewSet, CustomAuthToken

router = routers.DefaultRouter()
router.register('carts', CartViewSet)
router.register('orders', OrderViewSet)
router.register('products', ProductViewSet)
router.register('product_items', ProductItemViewSet)
router.register('warehouses', WarehouseViewSet)
router.register('auth/users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/auth/token/', CustomAuthToken.as_view()),
    path('api/', include(router.urls)),
]