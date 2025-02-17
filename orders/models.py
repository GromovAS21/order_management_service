from django.db import models

from dishes.models import Dish


class CHOICES_STATUS_ORDER(models.TextChoices):
    """Статусы Заказа"""

    ANTICIPATION = "anticipation", "В ожидании"
    READY = "ready", "Готово"
    PAID = "paid", "Оплачено"


class CHOICES_QUANTITY_SEAT(models.TextChoices):
    """Статусы Заказа"""

    ONE = "one", "1 персона"
    TWO = "two", "2 персоны"
    THREE = "three", "3 персоны"
    FOUR = "four", "4 персоны"
    FIVE = "five", "5 персон"


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
        max_length=20,
        choices=CHOICES_STATUS_ORDER,
        default=CHOICES_STATUS_ORDER.ANTICIPATION,
        verbose_name="Статус заказа",
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


class Table(models.Model):
    """Модель столов"""

    number = models.PositiveSmallIntegerField(verbose_name="Номер стола")
    quantity_seat = models.CharField(
        max_length=20,
        choices=CHOICES_QUANTITY_SEAT,
        default=CHOICES_QUANTITY_SEAT.ONE,
        verbose_name="Количество мест за столом",
    )

    def __str__(self):
        return f"Стол No {self.number}"

    class Meta:
        verbose_name = "Стол"
        verbose_name_plural = "Столы"
        ordering = ("-id",)
