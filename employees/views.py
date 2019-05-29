from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.shortcuts import get_object_or_404

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




# ------------------------------ ACCOUNTS - CLIENTS START ------------------------------ #
def view_clients(request):
    data = Client.objects.all()
    return render(request, template_name = 'create_accounts/view_clients.html', context = { 'data': data })

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

def edit_client(request, client_id):
    client = get_object_or_404(Client, pk = client_id)
    if request.method == "POST":
        form = AddClient(request.POST, instance = client)
        if form.is_valid():
            client = form.save(commit = False)
            client.save()
            return redirect('view_clients')
    else:
        form = AddClient(instance=client)
    return render(request, template_name = 'create_accounts/edit_client.html', context = { 'form': form })

def delete_client(request, client_id):
    client = Client.objects.filter(pk = client_id)
    if client:
        client = Client.objects.get(pk = client_id)
        client.delete()
    return redirect('view_clients')

# ------------------------------ ACCOUNTS - CLIENTS STOP ------------------------------ #


# ------------------------------ ACCOUNTS - EMPLOYEE START ------------------------------ #

def employee(request):
    employees = Employee.objects.all()
    return render(request, template_name = 'create_accounts/employees_list.html', context = { 'employees': employees })

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save(commit = False)
            employee.save()
            request.session['success'] = "Successfully added employee"
            return redirect('employee')
    else:
        form = EmployeeForm()

    return render(request, template_name = 'create_accounts/add_employee.html', context = { 'form': form })

# ------------------------------ ACCOUNTS - EMPLOYEE STOP ------------------------------ #


# ------------------------------ ACCOUNTS - DESIGNATION START ------------------------------ #
def designation(request):
    designation = Designation.objects.all()
    return render(request, template_name = 'create_accounts/designation.html', context = { 'designation': designation })

def add_designation(request):
    if request.method == 'POST':
        form = DesignationForm(request.POST)
        if form.is_valid():
            client = form.save(commit = False)
            client.save()
            request.session['success'] = "Successfully added designation"
            return redirect('designation')
    else:
        form = DesignationForm()

    return render(request, template_name = 'create_accounts/add_designation.html', context = { 'form': form })

def edit_designation(request, des_id):
    desi = get_object_or_404(Designation, pk = des_id)
    if request.method == "POST":
        form = DesignationForm(request.POST, instance = desi)
        if form.is_valid():
            desi = form.save(commit = False)
            desi.save()
            return redirect('designation')
    else:
        form = DesignationForm(instance = desi)
    return render(request, template_name = 'create_accounts/edit_designation.html', context = { 'form': form })

def delete_designation(request, des_id):
    des = Designation.objects.filter(pk = des_id)
    if des:
        des = Designation.objects.get(pk = des_id)
        des.delete()
    return redirect('designation')

# ------------------------------ ACCOUNTS - DESIGNATION STOP ------------------------------ #



# ------------------------------ ACCOUNTS - EMPLOYEE ACCESS START ------------------------------ #
def employee_access(request):
    return render(request, template_name = 'create_accounts/employee_access.html', context = { 'form': "rj" })

# ------------------------------ ACCOUNTS - EMPLOYEE ACCESS STOP ------------------------------ #



# ------------------------------ PROJECTS START ------------------------------ #

def projects(request):
    projects = Project.objects.all()
    return render(request, template_name = 'projects/projects_list.html', context = { 'projects': projects })

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.save()
            request.session['success'] = "Successfully added project"
            return redirect('projects')
    else:
        form = ProjectForm()

    return render(request, template_name = 'projects/add_project.html', context = { 'form': form })

def edit_project(request, project_id):
    project = get_object_or_404(Project, pk = project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance = project)
        if form.is_valid():
            project = form.save(commit = False)
            project.save()
            return redirect('projects')
    else:
        form = ProjectForm(instance = project)

    return render(request, template_name = 'projects/edit_project.html', context = { 'form': form })

def delete_project(request, project_id):
    project = Project.objects.filter(pk = project_id)
    if project:
        project = Project.objects.get(pk = project_id)
        project.delete()
    return redirect('projects')


def assign_project(request, project_id):
    if request.method == 'POST':
        form = ProjectAssignForm(request.POST)
        if form.is_valid():
            project = form.save(commit = False)
            project.save()
            request.session['success'] = "Successfully assigned project"
            return redirect('projects')
    else:
        form = ProjectAssignForm()

    return render(request, template_name = 'projects/assign_project.html', context = { 'form': form })

# ------------------------------ PROJECTS STOP ------------------------------ #



# ------------------------------ CAREERS - TECHNOLOGY START ------------------------------ #
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
    technology = get_object_or_404(Technology, pk = tech_id)
    if request.method == 'POST':
        form = TechnologyForm(request.POST, instance = technology)
        if form.is_valid():
            technology = form.save(commit = False)
            technology.save()
            return redirect('technology')
    else:
        form = TechnologyForm(instance = technology)

    return render(request, template_name = 'create_accounts/edit_technology.html', context = { 'form': form })

def delete_technology(request, tech_id):
    technology = Technology.objects.filter(pk = tech_id)
    if technology:
        technology = Technology.objects.get(pk = tech_id)
        technology.delete()
    return redirect('technology')

# ------------------------------ CAREERS - TECHNOLOGY STOP ------------------------------ #



# ------------------------------ CAREERS - INTERVIEW TRACKER START ------------------------------ #

def interview(request):
    interview = Interview.objects.all()
    return render(request, template_name = 'careers/interview.html', context = { "interview": interview })

def add_interview(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST, request.FILES)
        if form.is_valid():
            interview = form.save(commit = False)
            interview.save()
            request.session['success'] = "Successfully added Interview Schedule"
            return redirect('interview')
    else:
        form = InterviewForm()

    return render(request, template_name = 'careers/add_interview.html', context = { "form": form })

def edit_interview(request, inter_id):
    interview = get_object_or_404(Interview, pk = inter_id)
    if request.method == 'POST':
        form = InterviewForm(request.POST, instance = interview)
        if form.is_valid():
            interview = form.save(commit = False)
            interview.save()
            return redirect('interview')
    else:
        form = InterviewForm(instance = interview)

    return render(request, template_name = 'careers/edit_interview.html', context = { 'form': form })


def delete_interview(request, inter_id):
    interview = Interview.objects.filter(pk = inter_id)
    if interview:
        interview = Interview.objects.get(pk = inter_id)
        interview.delete()

    return redirect('interview')

# ------------------------------ CAREERS - INTERVIEW TRACKER STOP ------------------------------ #



# ------------------------------ PERFORMANCE - MANAGE QUESTION START ------------------------------ #

def question_list(request):
    questions = PerformanceQuestion.objects.all()
    return render(request, template_name = 'performance/question_list.html', context = { 'questions': questions })

def add_question(request):
    if request.method == 'POST':
        form = PerformanceQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit = False)
            question.save()
            return redirect('question_list')
    else:
        form = PerformanceQuestionForm()

    return render(request, template_name = 'performance/add_question.html', context = {'form': form})

def edit_question(request, ques_id):
    question = get_object_or_404(PerformanceQuestion, pk = ques_id)
    if request.method == 'POST':
        form = PerformanceQuestionForm(request.POST, instance = question)
        if form.is_valid():
            question = form.save(commit = False)
            question.save()
            return redirect('question_list')
    else:
        form = PerformanceQuestionForm(instance = question)

    return render(request, template_name = 'performance/edit_question.html', context = {'form': form})

def delete_question(request, ques_id):
    question = PerformanceQuestion.objects.filter(pk = ques_id)
    if question:
        question = PerformanceQuestion.objects.get(pk = ques_id)
        question.delete()

    return redirect('question_list')

# ------------------------------ PERFORMANCE - MANAGE QUESTION STOP ------------------------------ #



# ------------------------------ OTHERS - KNOWLEDGE ENTRY START ------------------------------ #

def knowledge(request):
    knowledge = Knowledge.objects.all()
    return render(request, template_name = 'others/knowledge.html', context = { 'knowledge': knowledge })

def add_knowledge(request):
    if request.method == 'POST':
        form = KnowledgeForm(request.POST, request.FILES)
        if form.is_valid():
            knowledge = form.save(commit = False)
            knowledge.save()
            return redirect('knowledge')
    else:
        form = KnowledgeForm()

    return render(request, template_name = 'others/add_knowledge.html', context = { 'form': form })

def edit_knowledge(request, know_id):
    knowledge = get_object_or_404(Knowledge, pk = know_id)
    if request.method == 'POST':
        form = KnowledgeForm(request.POST, request.FILES, instance = knowledge)
        if form.is_valid():
            knowledge = form.save(commit = False)
            knowledge.save()
            return redirect('knowledge')
    else:
        form = KnowledgeForm(instance = knowledge)

    return render(request, template_name = 'others/edit_knowledge.html', context = { 'form': form })

def delete_knowledge(request, know_id):
    knowledge = Knowledge.objects.filter(pk = know_id)
    if knowledge:
        knowledge = Knowledge.objects.get(pk = know_id)
        knowledge.delete()

    return redirect('knowledge')

# ------------------------------ OTHERS - KNOWLEDGE ENTRY STOP ------------------------------ #
