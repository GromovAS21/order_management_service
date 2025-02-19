from django import forms

from dishes.models import Dish
from orders.forms import StyleFormMixin


class DishForm(StyleFormMixin, forms.ModelForm):
    """Форма для добавления и изменения блюда"""

    class Meta:
        model = Dish
        fields = ("name", "price", "description")
