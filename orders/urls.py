from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from orders.apps import OrdersConfig
from orders.view_html import (
    OrderCreateView,
    OrderDeleteView,
    OrderDetailView,
    OrderListView,
    OrderUpdateView,
    calculation_revenue_view,
    search_view,
)
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
    path("orders/delete/<int:pk>/", OrderDeleteView.as_view(), name="orders_delete_html"),
    path("orders/revenue/", calculation_revenue_view, name="orders_revenue_html"),
    path("orders/search/", search_view, name="orders_search_html"),
    # Авторизация
    path("login/", LoginView.as_view(template_name="orders/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
