from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_todo, name="add_todo"),
    path(
        "edit_todo_item/<int:item_id>/", views.edit_todo, name="edit_todo"
    ),  # Correct URL pattern name
    path("delete/<int:todo_id>/", views.delete_todo, name="delete_todo"),
]
