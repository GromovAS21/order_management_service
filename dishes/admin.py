from django.contrib import admin

from dishes.models import Dish
from orders.models import Table


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    """Админка для Блюд"""

    list_display = ("id", "name", "price")
    search_fields = ("name",)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """Админка для Столов"""

    list_display = ("id", "number", "quantity_seat")
    search_fields = ("number",)
    list_filter = ("quantity_seat",)
