from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('login', views.loginView, name = 'login'),
    path('login_user', views.login_user, name = 'login_user'),
    path('logout', views.logout_user, name = 'logout'),

    # path('^', include('django.contrib.auth.urls')),
    # path(r'^password_reset/$', auth_views.password_reset),

    path('forgot_password', auth_views.PasswordChangeView.as_view(template_name='forgot_password.html'), name = 'forgot_password'),

    path('add_clients', views.add_clients, name = 'add_clients'),
    path('view_clients', views.view_clients, name = 'view_clients'),
]
