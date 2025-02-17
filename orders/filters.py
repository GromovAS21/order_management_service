from django_filters import rest_framework as filters

from orders.models import Order


class OrderFilter(filters.FilterSet):
    table_number = filters.NumberFilter(field_name="table_number__number")

    class Meta:
        model = Order
        fields = ["table_number", "status"]
