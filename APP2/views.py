from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def here_vision(request):
    return HttpResponse("HEY this is from app 2")
