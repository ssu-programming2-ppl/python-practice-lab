from django.shortcuts import render, redirect
import json
from core import utils
from main.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
import sys
sys.setrecursionlimit(10**7)
# Create your views here.


def index(request):
    # return render(request, "index.html")
    return redirect('overview')


def login_proc(request):
    if request.method == "GET":
        try:
            next = request.GET['next']
            next = str(next).split('//')[0]
            return render(request, 'login.html', {"next": next})
        except:
            return render(request, 'login.html', {"next": 'overview'})
    else:
        body = json.loads(request.body.decode('utf-8'))
        # user = User()
        username = body["email"]
        password = body["password"]
        next = body["next"]

        print(username)
        print(password)
        print(next)

        user = authenticate(email=username, password=password)
        if user is not None:
            login(request, user)
            return utils.create_ressult(next, "로그인 성공", True)

        return utils.create_ressult(None, "아이디를 확인해주세요", False)


def logout(request):
    logout(request)
    return render(request, "login.html")


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


@login_required(login_url='/login')
def overview(request):
    return render(request, "overview.html")


def handler404(request, exception, template_name="404.html"):
    response = render(template_name)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)


def handler403(request, *args, **argv):
    return render(request, '403.html', status=403)
