from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('login', views.loginView, name = 'login'),
    path('register', views.registerView, name = 'register'),
]
