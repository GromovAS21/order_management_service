from django.urls import path

from orders.apps import OrdersConfig
from orders.view_html import OrderCreateView, OrderDetailView, OrderListView, OrderUpdateView
from orders.views_api import CalculationRevenueAPIView, OrderAPIView, OrderDetailAPIView


app_name = OrdersConfig.name

urlpatterns = [
    # API
    path("api/orders/", OrderAPIView.as_view(), name="orders_list_create"),
    path("api/orders/<int:pk>/", OrderDetailAPIView.as_view(), name="orders_detail"),
    path("api/orders/total_revenue/", CalculationRevenueAPIView.as_view(), name="total_revenue"),
    # HTML
    path("orders/", OrderListView.as_view(), name="orders_list_html"),
    path("orders/create/", OrderCreateView.as_view(), name="orders_create_html"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="orders_detail_html"),
    path("orders/update/<int:pk>/", OrderUpdateView.as_view(), name="orders_update_html"),
]
