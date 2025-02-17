from django.contrib import admin


class DishAdmin(admin.ModelAdmin):
    """Админка для Блюд"""

    list_display = ("id", "name", "price")
    search_fields = ("name",)
