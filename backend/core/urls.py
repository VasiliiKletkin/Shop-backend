from carts.views import CartViewSet
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from orders.views import OrderViewSet
from products.views import ProductViewSet
from rest_framework import routers
from users.views import CustomAuthToken, UserViewSet

router = routers.DefaultRouter()
router.register('carts', CartViewSet)
router.register('orders', OrderViewSet)
router.register('products', ProductViewSet)
router.register('auth/users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('api/auth/token/', CustomAuthToken.as_view()),
    path('api/', include(router.urls)),
]
