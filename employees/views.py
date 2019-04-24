from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, template_name = 'dashboard.html')


def login(request):
    return HttpResponse("Login")


def loginView(request):
    return render(request, template_name = 'login.html')


def register(request):
    return HttpResponse("Register")


def registerView(request):
    return render(request, template_name = 'register.html')
