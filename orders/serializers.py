from rest_framework import serializers

from orders.models import Order


class OrderSerializers(serializers.ModelSerializer):
    """Сериализатор для Заказа"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["table_number"].required = True

    class Meta:
        model = Order
        fields = ("id", "table_number", "items", "total_price", "status", "datetime")
        read_only_fields = ("total_price",)
