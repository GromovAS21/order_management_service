import datetime
from typing import Union

from django.db.models import QuerySet

from orders.models import CHOICES_STATUS_ORDER, Order


class OrderService:
    """Сервис для работы с заказами"""

    @staticmethod
    def calculate_total_price(order: Order) -> float:
        """
        Метод для подсчета общей стоимости заказа

        :param: Заказ
        :return: Общая стоимость заказа
        """
        total_price = sum(item.price for item in order.items.all())
        return total_price

    @staticmethod
    def calculate_revenue() -> float:
        """
        Метод для подсчета выручки за смену

        :return: Общая выручка за смену
        """
        today = datetime.date.today()
        orders_paid = Order.objects.filter(status=CHOICES_STATUS_ORDER.PAID, datetime__date=today)

        if orders_paid:
            total_revenue = sum(order.total_price for order in orders_paid)
            return total_revenue

        return 0

    @staticmethod
    def number_of_lines(items: Union[list, QuerySet]) -> list[int]:
        """
        Метод для нумерации строк в списке
        """
        number = [number for number in range(1, len(items) + 1)]
        return number
