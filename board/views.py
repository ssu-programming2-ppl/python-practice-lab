from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from core import utils
from board.models import Board
from main.models import User
from django.db import transaction

# Create your views here.


def board_list(request):

    page = request.GET.get('page', '1')
    limit = request.GET.get('page', '10')

    # TODO(김금주) 게시판 목록 조회 개발 필요 ** 페이징 처리 필요
    return render(request, "board_list.html")


@login_required(login_url='/login')
@transaction.atomic()
def board_create(request):
    if request.method == "GET":
        return render(request, "board_create.html")
    else:
        body = json.loads(request.body.decode('utf-8'))
        board = Board()
        board.board_title = body['board_title']
        board.board_view_count = 0
        board.board_link = body['board_link']
        board.board_division = body['board_division']
        board.user_id = request.user
        board.save()

        return utils.create_ressult(None, "저장 성공", True)