from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from rest_framework import routers

from orders.apps import OrdersConfig
from orders.view_html import (
    OrderCreateView,
    OrderDeleteView,
    OrderDetailView,
    OrderListView,
    OrderUpdateView,
    TableCreateView,
    TableDeleteView,
    TableDetailView,
    TableListView,
    TableUpdateView,
    calculation_revenue_view,
    home_view,
    search_view,
)
from orders.views_api import CalculationRevenueAPIView, OrderAPIView, OrderDetailAPIView, TableViewSetAPIView


router = routers.DefaultRouter()
router.register(r"api/table", TableViewSetAPIView, basename="table")

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
    # Столы
    path("table/", TableListView.as_view(), name="table_list_html"),
    path("table/create/", TableCreateView.as_view(), name="table_create_html"),
    path("table/<int:pk>/", TableDetailView.as_view(), name="table_detail_html"),
    path("table/update/<int:pk>/", TableUpdateView.as_view(), name="table_update_html"),
    path("table/delete/<int:pk>/", TableDeleteView.as_view(), name="table_delete_html"),
    # Домашняя страница
    path("", home_view, name="home"),
] + router.urls
