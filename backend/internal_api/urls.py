from django.urls import path, include

app_name = "internal_api"

urlpatterns = [
    path('carts/', include('internal_api.carts_api.urls', namespace="carts")),
]
