"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from carts.views import CartViewSet
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from orders.views import OrderViewSet
from products.views import ProductItemViewSet, ProductViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)
from warehouses.views import WarehouseViewSet

router = routers.DefaultRouter()
router.register('carts', CartViewSet)
router.register('orders', OrderViewSet)
router.register('products', ProductViewSet)
router.register('product_items', ProductItemViewSet)
router.register('warehouses', WarehouseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),

    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/', include('djoser.urls')),

    path("api/", include(router.urls)),

    # path('carts/', include('carts.urls', namespace="carts_api")),
    # path('products/', include('products.urls',namespace='products_api')),
    # path('orders/', include('orders.urls', namespace='orders_api')),
    # path('warehouses/', include('warehouses.urls', namespace='warehouses_api')),

]
