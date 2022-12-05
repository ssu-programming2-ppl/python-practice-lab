from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_proc, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("register", views.register, name="register"),
    path("overview", views.overview, name="overview"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("test", views.test, name="test"),
]
