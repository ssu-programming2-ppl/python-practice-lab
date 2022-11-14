from django.shortcuts import render

# Create your views here.


def board_list(request):

    page = request.GET.get('page', '1')
    limit = request.GET.get('page', '10')

    #TODO(김금주) 게시판 목록 조회 개발 필요 ** 페이징 처리 필요
    return render(request, "board_list.html")


def board_create(request):

    if request.method == "GET":
        return render(request, "board_create.html")
    else:

        body = json.loads(request.body.decode('utf-8'))

        #TODO(김금주) 문제 생성 로직 필요
        # 1. body 변수에서 게시판 정보를 추출후 게시판 테이블에 저장
        return render(request, "board_create.html")
