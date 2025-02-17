from rest_framework import serializers

from dishes.models import Dish


class DishSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра Блюда"""

    class Meta:
        model = Dish
        fields = ("id", "name", "price", "description")
