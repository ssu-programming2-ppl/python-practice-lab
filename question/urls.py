from django.urls import path

from . import views


urlpatterns = [
    path("list", views.question_list, name="list"),
    path("create", views.question_create, name="create"),
    path("test", views.test, name="test"),
    path("<int:question_seq>/", views.question, name="question"),
]
