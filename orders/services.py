from orders.models import Order


class OrderService:
    """Сервис для работы с заказами"""

    @staticmethod
    def total_price(order: Order) -> float:
        """
        Метод для подсчета общей стоимости заказа
        :param Заказ
        :return: Общая стоимость заказа
        """

        total_price = 0

        for item in order.items.all():
            total_price += item.price

        return total_price
