import datetime

from django.db.models import QuerySet

from orders.models import CHOICES_STATUS_ORDER, Order


class OrderService:
    """Сервис для работы с заказами"""

    @staticmethod
    def calculate_total_price(order: Order) -> float:
        """
        Метод для подсчета общей стоимости заказа
        """
        total_price = sum(item.price for item in order.items.all())
        return total_price

    @staticmethod
    def calculate_revenue() -> float:
        """
        Метод для подсчета выручки за смену
        """
        today = datetime.date.today()
        orders_paid = Order.objects.filter(status=CHOICES_STATUS_ORDER.PAID, order_datetime__date=today)

        if orders_paid:
            total_revenue = sum(order.total_price for order in orders_paid)
            return total_revenue

        return 0

    @staticmethod
    def filter_orders_by_status() -> QuerySet:
        """
        Метод для фильтрации заказов по статусу
        """
        return Order.objects.filter().order_by("status")
