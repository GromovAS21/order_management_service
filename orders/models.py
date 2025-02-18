from django.db import models

from dishes.models import Dish


class CHOICES_STATUS_ORDER(models.TextChoices):
    """Статусы Заказа"""

    ANTICIPATION = "В ожидании", "В ожидании"
    READY = "Готово", "Готово"
    PAID = "Оплачено", "Оплачено"


class CHOICES_QUANTITY_SEAT(models.TextChoices):
    """Количество мест за столом"""

    ONE = "one", "1 персона"
    TWO = "two", "2 персоны"
    THREE = "three", "3 персоны"
    FOUR = "four", "4 персоны"
    FIVE = "five", "5 персон"


class Table(models.Model):
    """Модель столов"""

    number = models.PositiveSmallIntegerField(unique=True, verbose_name="Номер стола")
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


class Order(models.Model):
    """Модель Заказа"""

    table_number = models.ForeignKey(
        Table,
        on_delete=models.SET_NULL,
        verbose_name="Номер стола",
        null=True,
    )
    items = models.ManyToManyField(Dish, verbose_name="Блюда", blank=False)
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Общая стоимость заказа",
        help_text="Цена указывается в рублях",
        null=True,
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
        ordering = ("status",)
