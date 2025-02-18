from django.urls import path

from orders.apps import OrdersConfig
from orders.views import CalculationRevenueAPIView, OrderAPIView, OrderDetailAPIView


app_name = OrdersConfig.name

urlpatterns = [
    path("", OrderAPIView.as_view(), name="orders_list_create"),
    path("<int:pk>/", OrderDetailAPIView.as_view(), name="orders_detail"),
    path("total_revenue/", CalculationRevenueAPIView.as_view(), name="total_revenue"),
]
