from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from board.models import Board
from django.core.paginator import Paginator
import json


# Create your views here.


@login_required(login_url="/login")
def board_list(request):

    page = request.GET.get("page", "1")
    limit = request.GET.get("limit", "2")

    board_list = Board.objects.all().order_by("-board_seq")

    board_paginator = Paginator(board_list, limit)

    data = {
        "board_list": board_paginator.get_page(page),
    }

    # TODO(김금주) 게시판 목록 조회 개발 필요 ** 페이징 처리 필요
    return render(request, "board_list.html", data)


@login_required(login_url="/login")
def board_create(request):

    if request.method == "GET":
        return render(request, "board_create.html")
    else:

        body = json.loads(request.body.decode("utf-8"))

        # TODO(김금주) 문제 생성 로직 필요
        # 1. body 변수에서 게시판 정보를 추출후 게시판 테이블에 저장
        return render(request, "board_create.html")
