from django.shortcuts import render
from . import service
import json

# Create your views here.
def question_list(request):

    page = request.GET.get('page', '1')
    limit = request.GET.get('page', '10')

    #TODO(김금주) 문제 목록 조회 개발 필요 ** 페이징 처리 필요
    return render(request, "question_list.html")


def question_create(request):

    if request.method == "GET":
        return render(request, "question_create.html")
    else:

        body = json.loads(request.body.decode('utf-8'))

        #TODO(김금주) 문제 생성 로직 필요
        # 1. 문제 테이블에 문제 저장
        # 2. 배열로 들어온 테스트 케이스 테이블에 테스트 케이스 저장
        return render(request, "question_create.html")


def test(request):

    if not request.session.session_key:
        request.session.create()

    # 포스트 형식일시 채점 진행
    if request.method == "POST":

        session_id = request.session.session_key

        question_seq = request.POST["question_seq"]
        question_code = request.POST["question_code"]

        percent = service.scoring_question(session_id, question_seq, question_code)

        print(percent)

    return render(request, "test.html")


def question(request, question_seq):
    
    #TODO(김금주) 문제 조회 로직 필요
    # 1. question_seq 변수를 활용하여 문제 조회
    return render(request, "question.html")
