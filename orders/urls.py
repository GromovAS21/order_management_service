from django.urls import path

from orders.apps import OrdersConfig
from orders.view_html import OrderListView
from orders.views_api import CalculationRevenueAPIView, OrderAPIView, OrderDetailAPIView


app_name = OrdersConfig.name

urlpatterns = [
    # API
    path("api/orders/", OrderAPIView.as_view(), name="orders_list_create"),
    path("api/orders/<int:pk>/", OrderDetailAPIView.as_view(), name="orders_detail"),
    path("api/orders/total_revenue/", CalculationRevenueAPIView.as_view(), name="total_revenue"),
    # HTML
    path("orders/", OrderListView.as_view(), name="orders_list_html"),
]
