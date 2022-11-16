from django.shortcuts import render
from . import service
import json
from core import utils
from question.models import UserQuestionMap, Question

# Create your views here.
def question_list(request):

    page = request.GET.get('page', '1')
    limit = request.GET.get('page', '10')

    data = {
        "question_list" : Question.objects.all()
    }

    #TODO(김금주) 문제 목록 조회 개발 필요 ** 페이징 처리 필요
    return render(request, "question_list.html", data)


def question_create(request):

    if request.method == "GET":
        return render(request, "question_create.html")
    else:

        body = json.loads(request.body.decode('utf-8'))

        #TODO(김금주) 문제 생성 로직 필요
        # 1. 문제 테이블에 문제 저장
        # 2. 배열로 들어온 테스트 케이스 테이블에 테스트 케이스 저장
        return render(request, "question_create.html")


def question_submit(request):

    if not request.session.session_key:
        request.session.create()

    # 포스트 형식일시 채점 진행
    if request.method == "POST":
        
        session_id = request.session.session_key

        body = json.loads(request.body.decode('utf-8'))

        question_seq = body["question_seq"]
        question_code = body["question_code"]

        # 문제 맵핑 테이블이 없으면 새로 생성한다
        try:
            user_question_map_info = UserQuestionMap.objects.get(question_seq = question_seq, user_id = 'admin') 
        except UserQuestionMap.DoesNotExist:
            user_question_map_info = UserQuestionMap()
            user_question_map_info.question_seq = question_seq
            user_question_map_info.user_id = 'admin'
            user_question_map_info.question_correct_yn = 'N'
            user_question_map_info.question_save_yn = 'N'
            user_question_map_info.question_submit_count = 0

        # 점수
        percent = service.scoring_question(session_id, str(question_seq), question_code)

        # 100점이 넘으면 정탑 처리
        if percent >= 100:
            user_question_map_info.question_correct_yn = 'Y'

        # 제출 카운트 증가    
        user_question_map_info.question_submit_count += 1        
        user_question_map_info.save()

        print(percent)
        
    return utils.create_ressult(percent, "채점 성공", True)


def question(request, question_seq):

    data = {
        "question" : Question.objects.get(question_seq = question_seq) 
    }

    #TODO(김금주) 문제 조회 로직 필요
    # 1. question_seq 변수를 활용하여 문제 조회
    return render(request, "question.html", data)
