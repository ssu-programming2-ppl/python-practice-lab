from django.shortcuts import render

# Create your views here.


def list(request):
    return render(request, "board_list.html")


def create(request):
    return render(request, "board_create.html")
