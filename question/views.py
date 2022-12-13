from django.shortcuts import render, redirect
from . import service
import json
from core import utils
from question.models import UserQuestionMap, Question, Testcase
import datetime as dt
from django.db import transaction
from django.core.paginator import Paginator
from django.db.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def question_list(request):

    page = request.GET.get("page", "1")
    limit = request.GET.get("limit", "10")

    logined_user = request.user
    user_map = UserQuestionMap.objects.filter(
        user_id=logined_user, question_save_yn="Y"
    ).values_list("question_seq", flat=True)

    

    question_list = Question.objects.annotate(
        question_save_yn=Case(
            When(question_seq__in=user_map, then=Value("Y")),
            default=Value("N"),
        ),
        question_rating = Avg('question_map__question_rating'),
        question_submit_count=Sum(F("question_map__question_submit_count")),
    ).order_by("-created_at")

    paginator = Paginator(question_list, limit)

    data = {"question_list": paginator.get_page(page)}

    print(question_list.query)

    # TODO(김금주) 문제 목록 조회 개발 필요 ** 페이징 처리 필요
    return render(request, "question_list.html", data)


@login_required(login_url="/login")
@transaction.atomic()
def question_create(request):

    if request.method == "GET":
        return render(request, "question_create.html")
    else:

        body = json.loads(request.body.decode("utf-8"))
        question = Question()
        question.question_title = body["question_title"]
        question.question_level = body["question_level"]
        question.question_lang = body["question_lang"]
        question.question_text = body["question_text"]
        question.question_code = body["question_code"]
        question.question_creator = request.user
        question.save()

        testcase_list = body["testcase_list"]

        for tc in testcase_list:
            testcase = Testcase()
            testcase.testcase_input = tc["testcase_input"]
            testcase.testcase_output = tc["testcase_output"]
            testcase.testcase_open_yn = tc["testcase_open_yn"]
            testcase.question_seq = question

            testcase.save()

        return utils.create_ressult(None, "저장 성공", True)


@login_required(login_url="/login")
def question_excute(request):

    if request.method == "POST":
        body = json.loads(request.body.decode("utf-8"))

        question_seq = body["question_seq"]
        question_code = body["question_code"]

        result = service.excute_question(str(question_seq), question_code)

        return utils.create_ressult(result, "코드 실행 성공", True)


@login_required(login_url="/login")
def question_scoring(request):

    # 포스트 형식일시 채점 진행
    if request.method == "POST":

        body = json.loads(request.body.decode("utf-8"))

        logined_user = request.user

        question_seq = body["question_seq"]
        question_code = body["question_code"]
        question_start_time = body["question_start_time"]

        # 문제 맵핑 테이블이 없으면 새로 생성한다
        try:
            user_question_map_info = UserQuestionMap.objects.get(
                question_seq=question_seq, user_id=logined_user
            )
        except UserQuestionMap.DoesNotExist:
            user_question_map_info = UserQuestionMap()
            user_question_map_info.question_seq = Question.objects.get(
                question_seq=question_seq
            )
            user_question_map_info.user_id = logined_user
            user_question_map_info.question_correct_yn = "N"
            user_question_map_info.question_save_yn = "N"
            user_question_map_info.question_submit_count = 0

        # 점수
        percent = service.scoring_question(str(question_seq), question_code)

        # 100점이 넘으면 정탑 처리
        if percent >= 100:

            # 첫 정답이면 제출 카운트 증가
            if user_question_map_info.question_correct_yn == "N":
                user_question_map_info.question_submit_count += 1

            user_question_map_info.question_correct_yn = "Y"

            # 정답이면서 제출 시간이 기록 안됫으면 추가
            if (
                user_question_map_info.question_start_time == None
                and user_question_map_info.question_end_time == None
            ):
                user_question_map_info.question_start_time = question_start_time
                user_question_map_info.question_end_time = dt.datetime.now()
            else:
                prev = (
                    user_question_map_info.question_end_time
                    - user_question_map_info.question_start_time
                )
                now = dt.datetime.now() - dt.datetime.strptime(
                    question_start_time, "%Y-%m-%d %H:%M:%S.%f"
                )

                # 이미 제출 시간이 기록됫으면 현재 시간과 비교해서 수정
                if prev > now:
                    user_question_map_info.question_start_time = question_start_time
                    user_question_map_info.question_end_time = dt.datetime.now()

        # 정답을 못 맞췃으면 제출 카운트 증가
        else:
            user_question_map_info.question_submit_count += 1

        user_question_map_info.save()

        print(percent)

    return utils.create_ressult(percent, "채점 성공", True)


def question(request, question_seq):

    data = {"question": Question.objects.get(question_seq=question_seq)}

    # TODO(김금주) 문제 조회 로직 필요
    # 1. question_seq 변수를 활용하여 문제 조회
    return render(request, "question.html", data)


@login_required(login_url="/login")
def syntax_check(request):
    # 포스트 형식일시 코드 문법 검사
    if request.method == "POST":

        body = json.loads(request.body.decode("utf-8"))

        question_code = body["question_code"]

        flag, result = service.syntax_check(question_code)

        return utils.create_ressult(result, "문법 체크 성공", flag)


@login_required(login_url="/login")
def testcase_check(request):
    # 포스트 형식일시 테스트 케이스 검사
    print("zzz")
    if request.method == "POST":

        body = json.loads(request.body.decode("utf-8"))

        question_code = body["question_code"]
        testcase_list = body["testcase_list"]

        flag, result = service.syntax_check(question_code)

        if flag == False:
            return utils.create_ressult(result, "코드 문법 오류", flag)

        tc_list = []

        for i in range(len(testcase_list)):
            testcase = Testcase()
            testcase.testcase_input = testcase_list[i]["testcase_input"]
            testcase.testcase_output = testcase_list[i]["testcase_output"]
            testcase.testcase_seq = i
            tc_list.append(testcase)

        result, _ = service.scoring_code(question_code, tc_list)

        return utils.create_ressult(result, "테스트케이스 검사 완료", True)


@login_required(login_url="/login")
def question_save(request, question_seq):

    logined_user = request.user
    question = Question.objects.get(question_seq=question_seq)
    user_map, _ = UserQuestionMap.objects.get_or_create(
        user_id=logined_user, question_seq=question
    )

    if user_map.question_save_yn == "":
        user_map.question_save_yn = "Y"
        user_map.question_correct_yn = "N"

    elif user_map.question_save_yn == "N":
        user_map.question_save_yn = "Y"
    else:
        user_map.question_save_yn = "N"

    print(user_map.question_correct_yn)
    user_map.save()

    # return utils.create_ressult("", "저장(즐겨찾기) 완료", True)
    return redirect(request.META.get("HTTP_REFERER"))


@login_required(login_url="/login")
def question_rating(request):

    if request.method == "POST":

        body = json.loads(request.body.decode("utf-8"))
        user_map = UserQuestionMap.objects.get(
            user_id=request.user, question_seq=body["question_seq"]
        )
        user_map.question_rating = body["rate"]
        user_map.save()

        return utils.create_ressult("", "별점 등록 완료", True)    
    
    # return utils.create_ressult("", "지원하지 않ㅇ", True)    
