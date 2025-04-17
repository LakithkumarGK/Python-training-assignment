from django.shortcuts import render
from django.http import HttpResponse
from random import random


# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello, this is Home!</h1>")


def info(request):
    return HttpResponse("<h1>Hello UST, Welcome to Python Django Training!</h1>")

def index(request):
    # http://127.0.0.1:8000/index?dept=Marketing -> HTTP GET Request
    print(request.GET)
    dept = request.GET.get('dept')
    context = {
        'name' : 'Anil',
        'age'  : random.randint(1, 100),
        'dept' : dept
    }
    return render(request, 'firstapp/index.html', context)