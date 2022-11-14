from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def register(request):

    if request.method == "GET":
        return render(request, "register.html")
    else:

        body = json.loads(request.body.decode('utf-8'))

        #TODO(김금주) 회원가입 로직 필요
        # 1. body 변수에서 회원가입 정보를 추출후 사용자 테이블에 저장
        return render(request, "register.html")


def overview(request):
    return render(request, "overview.html")
