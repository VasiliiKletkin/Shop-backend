from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

app_name = "internal_api"

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/', include('djoser.urls')),

    path('carts/', include('internal_api.carts_api.urls', namespace="carts_api")),
    path('products/', include('internal_api.products_api.urls', namespace='products_api')),
    path('orders/', include('internal_api.orders_api.urls', namespace='orders_api')),
    path('warehouses/', include('internal_api.warehouses_api.urls', namespace='warehouses_api')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='internal_api:schema'), name='swagger-ui'),  
]