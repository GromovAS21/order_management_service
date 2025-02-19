import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from orders.forms import OrderCreateForm, OrderUpdateForm
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
    form_class = OrderCreateForm
    success_url = reverse_lazy("orders:orders_list_html")

    def form_valid(self, form) -> None:
        order = form.save()
        order.total_price = OrderService.calculate_total_price(order)
        order.save(update_fields=["total_price"])
        return super().form_valid(form)


class OrderDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для просмотра конкретного заказа"""

    model = Order


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования заказа"""

    model = Order
    form_class = OrderUpdateForm
    success_url = reverse_lazy("orders:orders_list_html")


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления заказа"""

    model = Order
    success_url = reverse_lazy("orders:orders_list_html")


@login_required
def calculation_revenue_view(request):
    """Контроллер для расчета выручки за смену"""

    total_revenue = OrderService.calculate_revenue()
    today = datetime.date.today()
    return render(request, "orders/calculation_revenue.html", {"total_revenue": total_revenue, "today": today})


@login_required
def search_view(request):
    """Контроллер для поиска заказов"""

    query = request.GET.get("query", "")
    orders_results = Order.objects.filter(Q(status__icontains=query) | Q(table_number__number__icontains=query))
    context = {
        "number": [number for number in range(1, len(orders_results) + 1)],
        "orders_results": orders_results,
    }
    return render(request, "orders/search_results.html", context)
