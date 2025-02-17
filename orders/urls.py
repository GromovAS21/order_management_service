from django.urls import path

from orders.apps import OrdersConfig
from orders.views import OrderAPIView


app_name = OrdersConfig.name

urlpatterns = [
    path("", OrderAPIView.as_view(), name="orders_list_create"),
]
