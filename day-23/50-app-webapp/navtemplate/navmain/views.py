from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'navmain/dashboard.html')


def incidents(request):
    return render(request, 'navmain/incidents.html')

 
def customers(request):
    return render(request, 'navmain/customers.html')


def about(request):
    return render(request, 'navmain/about.html')