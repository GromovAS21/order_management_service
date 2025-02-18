from django.forms import ModelForm

from orders.models import Order


class StyleFormMixin:
    """
    Mixin для стилизации формы.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class OrderForm(StyleFormMixin, ModelForm):
    """Форма для создания заказа"""

    class Meta:
        model = Order
        fields = ("table_number", "items")
