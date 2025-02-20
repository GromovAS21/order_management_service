from dishes.models import Dish


def create_test_dish():
    """Создание тестового блюда"""
    return Dish.objects.create(name="testdish", description="testtext", price=100)
