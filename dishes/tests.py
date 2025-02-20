from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from dishes.models import Dish


class DishTest(TestCase):
    """Тесты для объекта блюда"""

    def setUp(self):

        self.client = APIClient()
        self.user = User.objects.create_user(username="usertest", password="testpassword")
        self.dish = Dish.objects.create(name="testdish", description="testtext", price=100)

    def test_dish(self):
        """Тесты для объекта блюда"""
        print("asdasdasd", self.dish)
        self.assertEqual(self.dish.name, "testdish")
        self.assertEqual(self.dish.description, "testtext")
        self.assertEqual(self.dish.price, 100)

    def test_list_dish(self):
        """Тесты для списка блюд"""
        url = reverse("dishes:dish-list")
        # Неавторизованный пользователь
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 1)

    def test_create_dish(self):
        """Тесты для создания объекта блюда"""
        data = {"name": "testdish_1", "description": "testtext_1", "price": 100}
        url = reverse("dishes:dish-list")
        # Неавторизованный пользователь
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dish.objects.count(), 2)
        self.assertEqual(response.json()["name"], "testdish_1")
        self.assertEqual(response.json()["description"], "testtext_1")
        self.assertEqual(response.json()["price"], "100.00")

    def test_retrieve_dish(self):
        """Тесты для получения объекта блюда"""
        url = reverse("dishes:dish-detail", args=[self.dish.id])
        # Неавторизованный пользователь
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["name"], "testdish")
        self.assertEqual(response.json()["description"], "testtext")
        self.assertEqual(response.json()["price"], "100.00")

    def test_update_dish(self):
        """Тесты для обновления объекта блюда"""
        data = {"name": "testdish_2", "description": "testtext_2", "price": 1000}
        url = reverse("dishes:dish-detail", args=[self.dish.id])
        # Неавторизованный пользователь
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["name"], "testdish_2")
        self.assertEqual(response.json()["description"], "testtext_2")
        self.assertEqual(response.json()["price"], "1000.00")
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["name"], "testdish_2")
        self.assertEqual(response.json()["description"], "testtext_2")
        self.assertEqual(response.json()["price"], "1000.00")

    def test_delete_dish(self):
        """Тесты для удаления объекта блюда"""
        url = reverse("dishes:dish-detail", args=[self.dish.id])
        # Неавторизованный пользователь
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Dish.objects.count(), 0)
