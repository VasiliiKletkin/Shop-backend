from carts.views import CartAPI
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from orders.views import OrderViewSet
from products.views import ProductItemViewSet, ProductViewSet
from rest_framework import routers
from users.views import CustomAuthToken, UserViewSet

router = routers.DefaultRouter()
router.register('orders', OrderViewSet)
router.register('products', ProductViewSet)
router.register('product_items', ProductItemViewSet)
router.register('auth/users', UserViewSet)


api_urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('auth/token/', CustomAuthToken.as_view()),
    path('cart/', CartAPI.as_view()),
    path('', include(router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
]
