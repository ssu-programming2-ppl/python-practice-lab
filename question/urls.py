from django.urls import path

from . import views


urlpatterns = [
    path("list", views.question_list, name="list"),
    path("create", views.question_create, name="create"),
    path("scoring", views.question_scoring, name="scoring"),
    path("excute", views.question_excute, name="excute"),
    path("<int:question_seq>/", views.question, name="question"),
]
