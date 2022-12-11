from django.urls import path

from . import views


urlpatterns = [
    path("list", views.question_list, name="list"),
    path("create", views.question_create, name="create"),
    path("scoring", views.question_scoring, name="scoring"),
    path("excute", views.question_excute, name="excute"),
    path("rating", views.question_rating, name="rating"),
    path("syntax/check", views.syntax_check, name="syntax_check"),
    path("testcase/check", views.testcase_check, name="testcase_check"),
    path("<int:question_seq>/", views.question, name="question"),
    path("save/<int:question_seq>/", views.question_save, name="question_save"),
]
