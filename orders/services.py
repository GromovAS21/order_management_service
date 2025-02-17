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
