from django.contrib.auth.models import User

from orders.models import CHOICES_QUANTITY_SEAT, Table


def create_test_user():
    """Создание тестового пользователя"""
    return User.objects.create_user(username="testuser", password="testpassword")


def create_test_table():
    """Создание тестового стола"""
    return Table.objects.create(number=2, quantity_seat=CHOICES_QUANTITY_SEAT.ONE)
