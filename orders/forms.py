from django.forms import ModelForm

from orders.models import Order, Table


class StyleFormMixin:
    """
    Mixin для стилизации формы.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class OrderCreateForm(StyleFormMixin, ModelForm):
    """Форма для создания заказа"""

    class Meta:
        model = Order
        fields = ("table_number", "items")


class OrderUpdateForm(StyleFormMixin, ModelForm):
    """Форма для изменения заказа"""

    class Meta:
        model = Order
        fields = ("status",)


class TableForm(StyleFormMixin, ModelForm):
    """Форма для создания и обновлении стола"""

    class Meta:
        model = Table
        fields = ("number", "quantity_seat")
