import os
from django.http import JsonResponse

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Creating directory. " + directory)

def create_ressult(data, message, flag):        
    data = {
        "code": "0000" if flag else "9999",
        "data": data,
        "message": message,
        "flag" : flag
    }

    return JsonResponse(data)    