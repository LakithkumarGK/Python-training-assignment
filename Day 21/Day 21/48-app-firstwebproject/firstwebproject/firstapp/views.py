from django.shortcuts import render
from django.http import HttpResponse

import random

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

def age_check(request):
    context = {
        'name' : 'Anil',
        'age'  : str(random.randint(1, 30))
    }
    return render(request, 'firstapp/age_check.html', context) 

def fruit_list(request):
    fruitList = ['Apples', 'Mangoes', 'Cherries', 'Bananas']
    random.shuffle(fruitList)
    context = {
        'name' : 'Anil',
        'age'  : str(random.randint(1, 30)),
        'fruits' : fruitList
    }
    return render(request, 'firstapp/fruit_list.html', context) 

def input_form(request):
    return render(request, 'firstapp/input.html')

def result(request):
    print(request.method)
    print(request.POST)
    if request.method == 'POST': 
        name = request.POST.get('name', 'Unknown')
        age = request.POST.get('age', 'Unkown')
        context = {
            'name': name,
            'age' : age
        }
        return render(request, 'firstapp/output.html', context)
    else:
        return render(request, 'firstapp/input.html')
    
def timer_view(request):
    return render(request, 'firstapp/timer.html')
    



