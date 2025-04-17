from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello, this is Home!</h1>")


def info(request):
    return HttpResponse("<h1>Hello UST, Welcome to Python Django Training!</h1>")