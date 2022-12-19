from django.urls import path

from .views import (
  recipe_list_view,
  recipe_detail_view,
  recipe_create_view,
  recipe_update_view,
  recipe_delete_view,
  ingredient_delete_view,
)

app_name='recipes'

urlpatterns = [
  path("", recipe_list_view, name='list'),
  path("create/", recipe_create_view, name='create'),
  path("<int:id>/delete", recipe_delete_view, name='delete'),
  path("<int:id>/edit", recipe_update_view, name='update'),
  path("<int:parent_id>/ingredient/<int:id>/delete,", ingredient_delete_view, name='delete_recipe'),
  path("<int:id>/", recipe_detail_view, name='detail'),
]