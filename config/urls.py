from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from config import settings


schema_view = get_schema_view(
    openapi.Info(
        title="Сервис управления заказами",
        default_version="v1",
        description="Pet-проект сервиса для управления заказами в кафе",
        contact=openapi.Contact(email="GromovAS121@yandex.ru"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("orders.urls", namespace="orders")),
    path("", include("dishes.urls", namespace="dishes")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
