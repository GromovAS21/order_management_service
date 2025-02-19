from rest_framework import serializers

from dishes.serializers import DishSerializer
from orders.models import Order, Table


class TableSerializer(serializers.ModelSerializer):
    """Сериализатор для Стола"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["quantity_seat"].required = True

    class Meta:
        model = Table
        fields = ("id", "number", "quantity_seat")


class OrderCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания Заказа"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["table_number"].required = True

    class Meta:
        model = Order
        fields = ("id", "table_number", "items", "total_price", "status", "order_datetime")
        read_only_fields = ("total_price", "order_datetime", "status")


class OrderDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра Заказа"""

    table_number = TableSerializer()
    items = DishSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id", "table_number", "items", "total_price", "status", "order_datetime")


class OrderUpdateStatusSerializer(serializers.ModelSerializer):
    """Сериализатор для изменения статуса Заказа"""

    class Meta:
        model = Order
        fields = ("id", "table_number", "items", "total_price", "status", "order_datetime")
        read_only_fields = ("table_number", "items", "total_price", "order_datetime")


class CalculationRevenueSerializer(serializers.Serializer):
    """Сериализатор для расчета выручки"""

    total_revenue = serializers.IntegerField()
