from rest_framework import generics

from orders.models import Order
from orders.serializers import OrderDetailSerializers, OrderUpdateStatusSerializers
from orders.services import OrderService


class OrderAPIView(generics.ListCreateAPIView):
    """Представление создания и просмотр списка Заказов"""

    serializer_class = OrderDetailSerializers
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        order = serializer.save()
        order.total_price = OrderService.total_price(order)
        order.save(update_fields=["total_price"])


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для просмотра, изменения, удаления Заказа"""

    serializer_class = OrderDetailSerializers
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PUT" or self.request.method == "PATCH":
            return OrderUpdateStatusSerializers
        return OrderDetailSerializers
