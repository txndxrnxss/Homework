from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('home/', views.cookies_and_comm, name='home')
] 
