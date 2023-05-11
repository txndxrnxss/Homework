"""Настройка маршрутизации URL для Django-приложения blog."""

from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('home/', views.cookies_and_comm, name='home'),
    path('home/<post_id>', views.post_info, name='home_post_id')
] 