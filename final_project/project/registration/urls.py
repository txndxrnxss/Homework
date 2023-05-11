"""Настройка маршрутизации URL для Django-приложения registration."""

from django.urls import path
from . import views

app_name = 'registration'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.register, name='registration')
]