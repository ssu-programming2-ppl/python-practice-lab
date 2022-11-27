from django.shortcuts import render, redirect
import json
from core import utils
from main.models import User
from django.db import transaction
from django.core.paginator import Paginator
from django.contrib.auth import authenticate

# Create your views here.


def index(request):
    # return render(request, "index.html")
    return redirect('overview')


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:

        body = json.loads(request.body.decode('utf-8'))
        user = User()
        user.user_id = body["user_email"]
        user.user_password = body["user_password"]

        try:
            is_exist_user = User.objects.get(pk=user.user_id)
            print(is_exist_user.pk)
            return utils.create_ressult(None, "로그인 성공", True)
        except User.DoesNotExist:
            return utils.create_ressult(None, "아이디를 확인해주세요", False)


def register(request):

    if request.method == "GET":
        return render(request, "register.html")
    else:

        body = json.loads(request.body.decode('utf-8'))
        user = User()
        user.user_id = body["user_email"]
        user.user_password = body["user_password"]
        user.user_nickname = body["user_nickname"]

        try:
            is_exist_user = User.objects.get(pk=user.user_id)
            return utils.create_ressult(None, "이미 있는 회원입니다", False)
        except User.DoesNotExist:
            user.save()
            return utils.create_ressult(None, "회원가입 성공", True)


def overview(request):
    return render(request, "overview.html")