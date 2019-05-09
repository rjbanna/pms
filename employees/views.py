from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
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
            client.save()
            return render(request, template_name = 'create_accounts/add_clients.html', context = { 'form': form })
    else:
        form = AddClient()

    return render(request, template_name = 'create_accounts/add_clients.html', context = { 'form': form })

def view_clients(request):
    data = Client.objects.all()
    return render(request, template_name = 'create_accounts/view_clients.html', context = { 'data': data })


def edit_client(request, client_id):
    client = Client.objects.filter(pk = client_id)
    if client:
        client = Client.objects.get(pk = client_id)
        return render(request, template_name = 'create_accounts/edit_client.html', context = { 'client': client })


def delete_client(request, client_id):
    client = Client.objects.filter(pk = client_id)
    if client:
        client = Client.objects.get(pk = client_id)
        client.delete()
    return redirect('view_clients')


def add_designation(request):
    if request.method == 'POST':
        form = DesignationForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            request.session['success'] = "Successfully added designation"
            return redirect('designation')
    else:
        form = DesignationForm()

    return render(request, template_name = 'create_accounts/add_designation.html', context = { 'form': form })


def designation(request):
    designation = Designation.objects.all()
    return render(request, template_name = 'create_accounts/designation.html', context = { 'designation': designation })


def delete_designation(request, des_id):
    des = Designation.objects.filter(pk = des_id)
    if des:
        des = Designation.objects.get(pk = des_id)
        des.delete()
    return redirect('designation')



def technologies(request):
    technology = Technology.objects.all()
    return render(request, template_name = 'create_accounts/technology.html', context = { 'technology': technology })


def add_technology(request):
    if request.method == 'POST':
        form = TechnologyForm(request.POST)
        if form.is_valid():
            technology = form.save(commit=False)
            technology.save()
            request.session['success'] = "Successfully added technology"
            return redirect('technology')
    else:
        form = TechnologyForm()

    return render(request, template_name = 'create_accounts/add_technology.html', context = { 'form': form })

def edit_technology(request, tech_id):
    technology = Technology.objects.filter(pk = tech_id)
    if technology:
        technology = Technology.objects.get(pk = tech_id)
        return render(request, template_name = 'create_accounts/edit_client.html', context = { 'technology': technology })


def delete_technology(request, tech_id):
    technology = Technology.objects.filter(pk = tech_id)
    if technology:
        technology = Technology.objects.get(pk = tech_id)
        technology.delete()
    return redirect('technology')
