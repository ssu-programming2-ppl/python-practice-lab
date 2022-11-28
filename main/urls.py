from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_proc, name="login"),
    path("register", views.register, name="register"),
    path("overview", views.overview, name="overview"),
]
