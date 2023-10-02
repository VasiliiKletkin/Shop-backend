from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

app_name = "internal_api"

urlpatterns = [
    path('carts/', include('internal_api.carts_api.urls', namespace="carts_api")),
    path('products/', include('internal_api.products_api.urls', namespace='products')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name='internal_api:schema'), name='swagger-ui'),
]