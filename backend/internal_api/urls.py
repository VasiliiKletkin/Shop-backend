from django.urls import path, include

app_name = 'internal_api'

urlpatterns = [
path('products/', include('internal_api.products_api.urls', namespace='products')),
]
