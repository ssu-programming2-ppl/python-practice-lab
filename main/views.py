from django.shortcuts import render, redirect
import json
from core import utils
from main.models import User
from question.models import UserQuestionMap, Question
from django.db.models import F, Case, When, Value,Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
import sys

sys.setrecursionlimit(10**7)
# Create your views here.


def index(request):
    # return render(request, "index.html")
    return redirect("overview")


def login_proc(request):
    if request.method == "GET":
        try:
            next = request.GET["next"]
            next = str(next).split("//")[0]
            return render(request, "login.html", {"next": next})
        except:
            return render(request, "login.html", {"next": "overview"})
    else:
        body = json.loads(request.body.decode("utf-8"))
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

        body = json.loads(request.body.decode("utf-8"))
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


@login_required(login_url="/login")
def overview(request):
    logined_user = request.user

    # 생성 갯수 조회
    created_cnt = Question.objects.filter(user_id=logined_user).count()

    # 정답률 조회
    correct_cnt = UserQuestionMap.objects.filter(
        user_id=logined_user, question_correct_yn="Y"
    ).count()
    total_cnt = UserQuestionMap.objects.filter(user_id=logined_user).count()
    correct_rate = int((correct_cnt / total_cnt) * 100)

    user_map = UserQuestionMap.objects.filter(user_id=logined_user).values_list(
        "question_seq", flat=True
    )

    # 정답률로 비율 설정
    if correct_rate <= 30:
        level = "하"
    elif correct_rate <= 70:
        level = "중"
    else:
        level = "상"

    # 정해진 난이도로 5개 조회 및 제출이 많은 순으로 정렬 
    question_list = (
        Question.objects.filter(question_level=level)
        .annotate(
            question_save_yn=Case(
                When(
                    question_seq__in=user_map, then=F("question_map__question_save_yn")
                ),
                default=Value("N"),
            ),
            priority = Sum(F("question_map__question_submit_count"))
        )
        .order_by(F('priority').desc(nulls_last=True))[:5]
    )

    print(question_list.query)

    data = {
        "correct_rate": correct_rate,
        "created_cnt": created_cnt,
        "question_list": question_list,
    }

    return render(request, "overview.html", data)


@login_required(login_url='/login')
def overview(request):
    return render(request, "overview.html")


def handler404(request, exception, template_name="404.html"):
    response = render(template_name)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    return render(request, "500.html", status=500)


def handler403(request, *args, **argv):
    return render(request, '403.html', status=403)


def test(request):
    if request.method == "GET":
        return render(request, "test.html")
    else:
        return render(request, "test.html")
