from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from orders.models import CHOICES_QUANTITY_SEAT, Table


class TableTest(TestCase):
    """Тесты для стола"""

    def setUp(self):

        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.table = Table.objects.create(number=2, quantity_seat=CHOICES_QUANTITY_SEAT.ONE)

    def test_table(self):
        """Тесты для объекта стола"""
        self.assertEqual(self.table.number, 2)
        self.assertEqual(self.table.quantity_seat, "1 персона")

    def test_list_table(self):
        """Тесты для списка столов"""
        url = reverse("orders:table-list")
        # Неавторизованный пользователь
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 1)

    def test_create_table(self):
        """Тесты для создания объекта стола"""

        data = {
            "number": 3,
            "quantity_seat": CHOICES_QUANTITY_SEAT.TWO,
        }
        url = reverse("orders:table-list")
        # Неавторизованный пользователь
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_table(self):
        """Тесты для получения объекта стола"""
        url = reverse("orders:table-detail", args=[self.table.id])
        # Неавторизованный пользователь
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["number"], 2)
        self.assertEqual(response.json()["quantity_seat"], "1 персона")

    def test_update_table(self):
        """Тесты для обновления объекта стола"""
        data = {
            "number": 4,
            "quantity_seat": CHOICES_QUANTITY_SEAT.THREE,
        }
        url = reverse("orders:table-detail", args=[self.table.id])
        # Неавторизованный пользователь
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["number"], 4)
        self.assertEqual(response.json()["quantity_seat"], "3 персоны")
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["number"], 4)
        self.assertEqual(response.json()["quantity_seat"], "3 персоны")

    def test_delete_table(self):
        """Тесты для удаления объекта стола"""
        url = reverse("orders:table-detail", args=[self.table.id])
        # Неавторизованный пользователь
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Table.objects.count(), 0)
