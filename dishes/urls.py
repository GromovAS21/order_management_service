from django.urls import path

from dishes.apps import DishesConfig
from dishes.views_html import DishCreateView, DishDeleteView, DishDetailView, DishListView, DishUpdateView


app_name = DishesConfig.name

urlpatterns = [
    path("dishes/", DishListView.as_view(), name="dish_list_html"),
    path("dishes/create/", DishCreateView.as_view(), name="dish_create_html"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish_detail_html"),
    path("dishes/update/<int:pk>/", DishUpdateView.as_view(), name="dish_update_html"),
    path("dishes/delete/<int:pk>/", DishDeleteView.as_view(), name="dish_delete_html"),
]
