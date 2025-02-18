import datetime

from orders.models import Order


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
        orders_paid = Order.objects.filter(status="paid", datetime__date=today)

        if orders_paid:
            total_revenue = sum(order.total_price for order in orders_paid)
            return total_revenue

        return 0
