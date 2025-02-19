from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from dishes.models import Dish
from dishes.serializers import DishSerializer
from orders.views_api import manual_parameters_id, manual_parameters_query


class DishViewSetAPIView(viewsets.ModelViewSet):
    """Представление для просмотра, изменения, удаления Блюда>"""

    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    @swagger_auto_schema(
        operation_description="Получение списка всех блюд",
        operation_summary="Список Блюд",
        tags=["Блюдо"],
        manual_parameters=manual_parameters_query("блюд"),
        responses={
            200: openapi.Response(
                description="Успешный вывод списка блюд",
                schema=DishSerializer(),
            ),
            400: "Ошибка валидации",
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Создание нового блюда",
        operation_summary="Добавление Блюда",
        request_body=DishSerializer,
        tags=["Блюдо"],
        responses={
            201: openapi.Response(
                description="Блюдо успешно создано",
                schema=DishSerializer(),
            ),
            400: "Ошибка валидации",
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получение информации о блюде через идентификатор",
        operation_summary="Информация о блюде",
        tags=["Блюдо"],
        manual_parameters=manual_parameters_id("блюда"),
        responses={
            200: openapi.Response(
                description="Успешный вывод информации о блюде",
                schema=DishSerializer(),
            ),
            400: "Ошибка валидации",
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Полное изменение информации о блюде",
        operation_summary="Полное изменение блюда",
        tags=["Блюдо"],
        request_body=DishSerializer,
        manual_parameters=manual_parameters_id("блюда"),
        responses={
            200: openapi.Response(
                description="Успешное полное изменение информации о блюде",
                schema=DishSerializer(),
            ),
            400: "Ошибка валидации",
        },
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частичное изменение информации о блюде",
        operation_summary="Частичное изменение блюда",
        tags=["Блюдо"],
        request_body=DishSerializer,
        manual_parameters=manual_parameters_id("блюда"),
        responses={
            200: openapi.Response(
                description="Успешное частичное изменение информации о блюде",
                schema=DishSerializer(),
            ),
            400: "Ошибка валидации",
        },
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удаление информации о блюде",
        operation_summary="Удаление блюда",
        tags=["Блюдо"],
        manual_parameters=manual_parameters_id("блюда"),
        responses={
            204: openapi.Response(
                description="Успешное удаление информации о блюде",
            ),
            400: "Ошибка валидации",
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
