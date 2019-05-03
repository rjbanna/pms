from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, AddClient
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
        request.session['error'] = "Username or Password is incorrect"
        return redirect('login')


def loginView(request):
    if 'username' in request.session:
        return redirect('dashboard')
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password = password)
            if user != None:
                login(request, user)
                request.session['username'] = username
                request.session['designation'] = str(user.profile.designation)
                return redirect('dashboard')
            else:
                request.session['error'] = "Username or Password is incorrect"
                return redirect('login')

    else:
        form = LoginForm()

    return render(request, template_name = 'login.html', context = { 'form': form })

def logout_user(request):
    del request.session['username']
    logout(request)
    return redirect('login')


def forgot_password(request):
    del request.session['username']
    logout(request)
    return redirect('login')


def add_clients(request):
    if request.method == 'POST':
        form = AddClient(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            return render(request, template_name = 'create_accounts/add_clients.html', context = { 'client': client })
            client.author = request.user
            client.published_date = timezone.now()
            client.save()
            return redirect('post_detail', pk=client.pk)
            # return render(request, template_name = 'create_accounts/add_clients.html', context = { 'form': form })
    else:
        form = AddClient()

    return render(request, template_name = 'create_accounts/add_clients.html', context = { 'form': form })

def view_clients(request):
    return render(request, template_name = 'create_accounts/view_clients.html')
