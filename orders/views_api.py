from typing import Type

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from orders.filters import OrderFilter
from orders.models import Order
from orders.serializers import OrderCreateSerializer, OrderDetailSerializer, OrderUpdateStatusSerializer
from orders.services import OrderService


manual_parameters = [
    openapi.Parameter(
        name="id",
        in_=openapi.IN_PATH,
        type=openapi.TYPE_INTEGER,
        description="Уникальный идентификатор Заказа в базе данных",
        required=True,
    )
]


class OrderAPIView(generics.ListCreateAPIView):
    """Представление создания и просмотр списка Заказов"""

    queryset = Order.objects.all()
    filterset_class = OrderFilter

    @swagger_auto_schema(
        operation_description="Создание нового заказа",
        operation_summary="Добавление Заказа",
        request_body=OrderCreateSerializer,
        tags=["Заказ"],
        responses={
            201: openapi.Response(
                description="Заказ успешно создан",
                schema=OrderCreateSerializer(),
            ),
            400: "Ошибка валидации",
        },
    )
    def post(self, request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение списка всех заказов с развернутой информацией о столах и блюдах",
        operation_summary="Список Заказов",
        tags=["Заказ"],
        manual_parameters=[
            openapi.Parameter(
                name="limit",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Количество заказов для возврата на страницу",
                required=False,
            ),
            openapi.Parameter(
                name="offset",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Начальный индекс для пагинации",
            ),
        ],
        responses={
            200: openapi.Response(
                description="Успешый вывод списка заказов",
                schema=OrderDetailSerializer(),
            ),
            400: "Ошибка валидации",
        },
    )
    def get(self, request, *args, **kwargs) -> Response:
        return super().get(request, *args, **kwargs)

    def perform_create(self, serializer) -> None:
        order = serializer.save()
        order.total_price = OrderService.calculate_total_price(order)
        order.save(update_fields=["total_price"])

    def get_serializer_class(self) -> Type[Serializer]:
        if self.request.method == "POST":
            return OrderCreateSerializer
        return OrderDetailSerializer


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для просмотра, изменения, удаления Заказа"""

    queryset = Order.objects.all()

    def get_serializer_class(self) -> Type[Serializer]:
        if self.request.method == "PUT" or self.request.method == "PATCH":
            return OrderUpdateStatusSerializer
        return OrderDetailSerializer

    @swagger_auto_schema(
        operation_description="Получение информации о заказе через идентификатор",
        operation_summary="Информация о заказе",
        tags=["Заказ"],
        manual_parameters=manual_parameters,
        responses={
            200: openapi.Response(
                description="Успешный вывод информации о заказе",
                schema=OrderDetailSerializer(),
            ),
            400: "Ошибка валидации",
        },
    )
    def get(self, request, *args, **kwargs) -> Response:
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частичное изменение информации о заказе",
        operation_summary="Частичное изменение заказа",
        tags=["Заказ"],
        request_body=OrderUpdateStatusSerializer,
        manual_parameters=manual_parameters,
        responses={
            200: openapi.Response(
                description="Успешное частичное изменение информации о заказе",
                schema=OrderUpdateStatusSerializer(),
            ),
            400: "Ошибка валидации",
        },
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Полное изменение информации о заказе",
        operation_summary="Полное изменение заявки",
        tags=["Заказ"],
        request_body=OrderUpdateStatusSerializer,
        manual_parameters=manual_parameters,
        responses={
            200: openapi.Response(
                description="Успешный полное изменение информации о заказе",
                schema=OrderUpdateStatusSerializer(),
            ),
            400: "Ошибка валидации",
        },
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удаление информации о заказе",
        operation_summary="Удаление заявки",
        tags=["Заказ"],
        manual_parameters=manual_parameters,
        responses={
            204: openapi.Response(
                description="Успешное удаление информации о заказе",
            ),
            400: "Ошибка валидации",
        },
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class CalculationRevenueAPIView(APIView):
    """Представление для расчета выручки за смену"""

    def get(self, request, *args, **kwargs):
        total_revenue = OrderService.calculate_revenue()

        if total_revenue:
            return Response({"total_revenue": total_revenue})
        return Response({"total_revenue": 0})
