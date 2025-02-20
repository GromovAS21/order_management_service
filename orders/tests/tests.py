import datetime

from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from dishes.tests.fixtures import create_test_dish
from orders.models import CHOICES_QUANTITY_SEAT, CHOICES_STATUS_ORDER, Order, Table
from orders.tests.fixtures import create_test_order, create_test_table, create_test_user


class TableTest(TestCase):
    """Тесты для стола"""

    def setUp(self):

        self.client = APIClient()
        self.user = create_test_user()
        self.table = create_test_table()

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


class OrderTest(TestCase):
    """Тесты для заказа"""

    def setUp(self):
        self.client = APIClient()
        self.user = create_test_user()
        self.table = create_test_table()
        self.dish = create_test_dish()
        self.order = create_test_order(self.table, self.dish)

    def test_order(self):
        """Тесты для объекта заказа"""
        self.assertEqual(self.order.table_number.number, self.table.number)
        self.assertEqual(self.order.items.all()[0].name, self.dish.name)

    def test_list_order(self):
        """Тесты для списка заказов"""
        url = reverse("orders:orders_list_create")
        # Неавторизованный пользователь
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()["results"]), 1)

    def test_create_order(self):
        """Тесты для создания объекта заказа"""
        data = {
            "table_number": self.table.id,
            "items": [self.dish.id],
        }
        url = reverse("orders:orders_list_create")
        # Неавторизованный пользователь
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()["table_number"], 1)
        self.assertEqual(response.json()["items"][0], self.dish.id)
        self.assertEqual(response.json()["total_price"], "100.00")
        self.assertEqual(response.json()["status"], "В ожидании")
        today_date = datetime.date.today()
        self.assertEqual(response.data["order_datetime"][:10], str(today_date))

    def test_retrieve_order(self):
        """Тесты для получения объекта заказа"""
        url = reverse("orders:orders_detail", args=[self.order.id])
        # Неавторизованный пользователь
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["table_number"]["number"], 2)
        self.assertEqual(response.json()["items"][0]["id"], self.dish.id)
        self.assertEqual(response.json()["total_price"], "100.00")
        self.assertEqual(response.json()["status"], CHOICES_STATUS_ORDER.ANTICIPATION)

    def test_update_order(self):
        """Тесты для обновления объекта заказа"""
        data = {"status": CHOICES_STATUS_ORDER.PAID}
        url = reverse("orders:orders_detail", args=[self.order.id])
        # Неавторизованный пользователь
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["status"], CHOICES_STATUS_ORDER.PAID)
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["status"], CHOICES_STATUS_ORDER.PAID)

    def test_delete_order(self):
        """Тесты для удаления объекта заказа"""
        url = reverse("orders:orders_detail", args=[self.order.id])
        # Неавторизованный пользователь
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)

    def test_total_revenue(self):
        """Тесты для получения общей суммы заказов"""
        url = reverse("orders:total_revenue")
        # Неавторизованный пользователь
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Авторизованный пользователь
        self.client.force_authenticate(user=self.user)
        # Если нет статуса "Оплачено"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["total_revenue"], 0)
        # Меняем на статус оплачено
        data = {"status": CHOICES_STATUS_ORDER.PAID}
        self.client.patch(reverse("orders:orders_detail", args=[self.order.id]), data)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["total_revenue"], 100.00)
