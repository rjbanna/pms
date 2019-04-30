from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, template_name = 'dashboard.html', context = {'user': request.user})


def login_user(request):
    if 'error' in request.session:
        del request.session['error']

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username, password = password)
    if user != None:
        login(request, user)
        request.session['username'] = username
        request.session['designation'] = str(user.profile.designation)
        return redirect('dashboard')
    else:
        # CHECK FOR ERROR IN LOGIN AND DISPLAY THERE (USE THIS WAY FOR ANY ERROR)
        request.session['error'] = "Username or Password is incorrect"
        return redirect('login')


def loginView(request):
    if 'username' in request.session:
        return redirect('dashboard')
    else:
        return render(request, template_name = 'login.html')

def logout_user(request):
    del request.session['username']
    logout(request)
    return redirect('login')


def forgot_password(request):
    del request.session['username']
    logout(request)
    return redirect('login')
