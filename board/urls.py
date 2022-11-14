from django.urls import path

from . import views


urlpatterns = [
    path("list", views.board_list, name="list"),
    path("create", views.board_create, name="create"),
]
