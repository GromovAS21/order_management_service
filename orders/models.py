from django.db import models

from dishes.models import Dish


class CHOICES_STATUS_ORDER(models.TextChoices):
    """Статусы Заказа"""

    ANTICIPATION = "Anticipation", "В ожидании"
    READY = "Ready", "Готово"
    PAID = "Paid", "Оплачено"


class Order(models.Model):
    """Модель Заказа"""

    table_number = models.PositiveSmallIntegerField(
        verbose_name="Номер стола",
    )
    items = models.ManyToManyField(Dish, verbose_name="Блюда", blank=True)
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Общая стоимость заказа",
    )
    status = models.CharField(
        max_length=20, choices=CHOICES_STATUS_ORDER, default="Anticipation", verbose_name="Статус заказа"
    )

    datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время заказа",
    )

    def __str__(self):
        return f"Заказ No {self.id}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ("-id",)
