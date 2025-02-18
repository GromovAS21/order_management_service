from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from orders.forms import OrderForm
from orders.models import Order
from orders.services import OrderService


class OrderListView(LoginRequiredMixin, ListView):
    """
    Контроллер для отображения всех заказов
    """

    model = Order
    queryset = Order.objects.all()

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["number"] = [number for number in range(1, len(context["object_list"]) + 1)]
        return context


class OrderCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания заказа"""

    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("orders:orders_list_html")

    def form_valid(self, form) -> None:
        order = form.save()
        order.total_price = OrderService.calculate_total_price(order)
        order.save(update_fields=["total_price"])
        return super().form_valid(form)


class OrderDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для просмотра конкретного заказа"""

    model = Order
