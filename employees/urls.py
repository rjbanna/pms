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

    path('client', views.view_clients, name = 'view_clients'),
    path('client/add', views.add_clients, name = 'add_clients'),
    path('client/<int:client_id>/edit', views.edit_client, name = 'edit_client'),
    path('client/<int:client_id>/delete', views.delete_client, name = 'delete_client'),

    path('designation', views.designation, name = 'designation'),
    path('designation/add', views.add_designation, name = 'add_designation'),
    path('designation/<int:des_id>/edit', views.edit_designation, name = 'edit_designation'),
    path('designation/<int:des_id>/delete', views.delete_designation, name = 'delete_designation'),

    path('technology', views.technologies, name = 'technology'),
    path('technology/add', views.add_technology, name = 'add_technology'),
    path('technology/<int:tech_id>/edit', views.edit_technology, name = 'edit_technology'),
    path('technology/<int:tech_id>/delete', views.delete_technology, name = 'delete_technology'),

    path('career/interview', views.interview, name = 'interview'),
    path('career/interview/add', views.add_interview, name = 'add_interview'),
    path('career/interview/<int:inter_id>/edit', views.edit_interview, name = 'edit_interview'),
    path('career/interview/<int:inter_id>/delete', views.delete_interview, name = 'delete_interview'),

    path('employee/access', views.employee_access, name = 'employee_access'),
]
