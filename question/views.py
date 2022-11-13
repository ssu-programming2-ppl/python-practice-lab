from django.shortcuts import render
from . import service

# Create your views here.
def list(request):
    return render(request, "question_list.html")


def create(request):
    return render(request, "question_create.html")


def test(request):

    if not request.session.session_key:
        request.session.create()

    # 포스트 형식일시 채점 진행
    if request.method == "POST":

        session_id = request.session.session_key

        question_seq = request.POST["question_seq"]
        question_code = request.POST["question_code"]

        percent = service.scoringQuestion(session_id, question_seq, question_code)

        print(percent)

    return render(request, "test.html")


def question(request):
    return render(request, "question.html")
