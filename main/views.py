from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def login(request):
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')

def list(request):
    return render(request, 'main/list.html')

def create(request):
    return render(request, 'main/create.html')

def test(request):
    return render(request, 'main/test.html')

def board(request):
    return render(request, 'main/board.html')

def overview(request):
    return render(request, 'main/overview.html')

def question(request):
    seq = request.GET.get('questionSeq', str(1))
    data = getQuestionInfo(seq)
    print(data)
    
    return render(request, 'main/question.html', data)

def getQuestionInfo(seq):

    data = {
        "question_seq": "test data1 " + seq,
        "question_title": "test data2 " + seq,
        "question_level": "test data3 " + seq,
        "question_rating": "test data4 " + seq,
        "question_lang": "test data5 " + seq,
        "question_text": "test data6 " + seq,
        "question_code": "test data7 " + seq,
        "created_at": "test data8 " + seq,
        "modified_at": "test data9 " + seq,
        "user_id": "test data10 " + seq
    }

    return data