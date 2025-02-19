from django.contrib import admin

from dishes.models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    """Админка для Блюд"""

    list_display = ("id", "name", "price")
    search_fields = ("name",)
