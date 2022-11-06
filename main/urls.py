from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('list', views.list, name='list'),
    path('create', views.create, name='create'),
    path('test', views.test, name='test'),
    path('question', views.question, name='question'),
    path('overview', views.overview, name='overview'),
    path('board', views.board, name='board')
]