from django.db import models


class Dish(models.Model):
    """Модель Блюд"""

    name = models.CharField(max_length=100, verbose_name="Названия блюда")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(verbose_name="Описание блюда", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
        ordering = ("name",)
