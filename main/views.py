from django.shortcuts import render, redirect
import json
from core import utils
from main.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password

# Create your views here.


def index(request):
    # return render(request, "index.html")
    return redirect('overview')


def login_proc(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:

        body = json.loads(request.body.decode('utf-8'))
        # user = User()
        username = body["email"]
        password = body["password"]

        print(username)
        print(password)

        user = authenticate(email=username, password=password)
        print(user)
        if user is not None:
            login(request, user)     
            return utils.create_ressult(None, "로그인 성공", True)   

        return utils.create_ressult(None, "아이디를 확인해주세요", False)
        # try:
        #     is_exist_user = User.objects.get(pk=user.user_id)
        #     print(is_exist_user.pk)
        #     return utils.create_ressult(None, "로그인 성공", True)
        # except User.DoesNotExist:
        #     return utils.create_ressult(None, "아이디를 확인해주세요", False)


def register(request):

    if request.method == "GET":
        return render(request, "register.html")
    else:

        body = json.loads(request.body.decode('utf-8'))
        user = User()
        user.email = body["email"]
        user.password = make_password(body["password"])
        user.nickname = body["nickname"]
        print(make_password(user.password))

        try:
            is_exist_user = User.objects.get(pk=user.email)
            return utils.create_ressult(None, "이미 있는 회원입니다", False)
        except User.DoesNotExist:
            user.save()
            return utils.create_ressult(None, "회원가입 성공", True)


def overview(request):
    return render(request, "overview.html")