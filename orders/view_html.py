from django.views.generic import ListView

from orders.models import Order


class OrderListView(ListView):
    """
    Контроллер для отображения всех заказов
    """

    model = Order
    queryset = Order.objects.all()
