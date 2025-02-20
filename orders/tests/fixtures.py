import datetime

from django.contrib.auth.models import User

from dishes.tests.fixtures import create_test_dish
from orders.models import CHOICES_QUANTITY_SEAT, Order, Table


def create_test_user():
    """Создание тестового пользователя"""
    return User.objects.create_user(username="testuser", password="testpassword")


def create_test_table():
    """Создание тестового стола"""
    return Table.objects.create(number=2, quantity_seat=CHOICES_QUANTITY_SEAT.ONE)


def create_test_order(table, dish):
    """Создание тестового заказа"""
    today_date = datetime.datetime.now()
    order = Order.objects.create(table_number=table, total_price="100.00", order_datetime=today_date)
    order.items.add(dish)
    return order
