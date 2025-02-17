from rest_framework import generics

from orders.filters import OrderFilter
from orders.models import Order
from orders.serializers import OrderCreateSerializers, OrderDetailSerializers, OrderUpdateStatusSerializers
from orders.services import OrderService


class OrderAPIView(generics.ListCreateAPIView):
    """Представление создания и просмотр списка Заказов"""

    queryset = Order.objects.all()
    filterset_class = OrderFilter

    def perform_create(self, serializer):
        order = serializer.save()
        order.total_price = OrderService.total_price(order)
        order.save(update_fields=["total_price"])

    def get_serializer_class(self):
        if self.request.method == "POST":
            return OrderCreateSerializers
        return OrderDetailSerializers


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для просмотра, изменения, удаления Заказа"""

    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PUT" or self.request.method == "PATCH":
            return OrderUpdateStatusSerializers
        return OrderDetailSerializers
