from django.urls import path

from . import views


urlpatterns = [
    path("list", views.list, name="list"),
    path("create", views.create, name="create"),
    path("test", views.test, name="test"),
    path("", views.question, name="question"),
]
