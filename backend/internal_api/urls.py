from django.urls import path, include

app_name = "internal_api"

urlpatterns = [
    path('carts/', include('internal_api.carts_api.urls', namespace="carts_api")),
    path('products/', include('internal_api.products_api.urls', namespace='products_api')),
    path('orders/', include('internal_api.orders_api.urls', namespace='orders_api')),
    path('warehouses/', include('internal_api.warehouses_api.urls', namespace='warehouses_api')),
]
