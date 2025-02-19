from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from dishes.forms import DishForm
from dishes.models import Dish
from orders.services import number_of_lines


class DishListView(LoginRequiredMixin, ListView):
    """Контроллер для отображения всех блюд"""

    model = Dish
    queryset = Dish.objects.all()

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["number"] = number_of_lines(context["object_list"])
        return context


class DishCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания блюда"""

    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("dishes:dish_list_html")


class DishDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для просмотра конкретного блюда"""

    model = Dish


class DishUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования блюда"""

    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("dishes:dish_list_html")


class DishDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления блюда"""

    model = Dish
    success_url = reverse_lazy("dishes:dish_list_html")
