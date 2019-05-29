from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('login', views.loginView, name = 'login'),
    path('login_user', views.login_user, name = 'login_user'),
    path('logout', views.logout_user, name = 'logout'),

    path('forgot_password', auth_views.PasswordChangeView.as_view(template_name='forgot_password.html'), name = 'forgot_password'),

    # -------------------- ACCOUNTS --------------------#

    path('employee', views.employee, name = 'employee'),
    path('employee/add', views.add_employee, name = 'add_employee'),

    path('client', views.view_clients, name = 'view_clients'),
    path('client/add', views.add_clients, name = 'add_clients'),
    path('client/<int:client_id>/edit', views.edit_client, name = 'edit_client'),
    path('client/<int:client_id>/delete', views.delete_client, name = 'delete_client'),

    path('employee/access', views.employee_access, name = 'employee_access'),

    path('designation', views.designation, name = 'designation'),
    path('designation/add', views.add_designation, name = 'add_designation'),
    path('designation/<int:des_id>/edit', views.edit_designation, name = 'edit_designation'),
    path('designation/<int:des_id>/delete', views.delete_designation, name = 'delete_designation'),

    # -------------------- ACCOUNTS END --------------------#

    # -------------------- PROJECTS --------------------#

    path('projects', views.projects, name = 'projects'),
    path('project/add', views.add_project, name = 'add_project'),
    path('project/<int:project_id>/edit', views.edit_project, name = 'edit_project'),
    path('project/<int:project_id>/delete', views.delete_project, name = 'delete_project'),

    path('project/<int:project_id>/assign', views.assign_project, name = 'assign_project'),

    # -------------------- PROJECTS --------------------#

    # -------------------- CAREERS --------------------#

    path('career/interview', views.interview, name = 'interview'),
    path('career/interview/add', views.add_interview, name = 'add_interview'),
    path('career/interview/<int:inter_id>/edit', views.edit_interview, name = 'edit_interview'),
    path('career/interview/<int:inter_id>/delete', views.delete_interview, name = 'delete_interview'),

    path('technology', views.technologies, name = 'technology'),
    path('technology/add', views.add_technology, name = 'add_technology'),
    path('technology/<int:tech_id>/edit', views.edit_technology, name = 'edit_technology'),
    path('technology/<int:tech_id>/delete', views.delete_technology, name = 'delete_technology'),

    # -------------------- CAREERS END --------------------#

    # -------------------- PERFORMANCE --------------------#

    path('performance/questions', views.question_list, name = 'question_list'),
    path('performance/question/add', views.add_question, name = 'add_question'),
    path('performance/question/<int:ques_id>/edit', views.edit_question, name = 'edit_question'),
    path('performance/question/<int:ques_id>/delete', views.delete_question, name = 'delete_question'),

    # -------------------- PERFORMANCE END --------------------#

    # -------------------- OTHERS --------------------#

    path('knowledge', views.knowledge, name = 'knowledge'),
    path('knowledge/add', views.add_knowledge, name = 'add_knowledge'),
    path('knowledge/<int:know_id>/edit', views.edit_knowledge, name = 'edit_knowledge'),
    path('knowledge/<int:know_id>/delete', views.delete_knowledge, name = 'delete_knowledge'),

    # -------------------- OTHERS END --------------------#
]
