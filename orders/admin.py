from django.contrib import admin

from orders.models import Order, Table


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админка для Заказа"""

    list_display = ("id", "order_datetime", "table_number", "total_price", "status")
    list_filter = ("status",)
    search_fields = ("id",)
    readonly_fields = ("order_datetime",)


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    """Админка для Столов"""

    list_display = ("id", "number", "quantity_seat")
    list_filter = ("quantity_seat",)
    search_fields = ("id",)
