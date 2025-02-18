from django.views.generic import ListView

from orders.models import Order


class OrderListView(ListView):
    """
    Контроллер для отображения всех заказов
    """

    model = Order
    queryset = Order.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["number"] = [number for number in range(1, len(context["object_list"]) + 1)]
        return context
