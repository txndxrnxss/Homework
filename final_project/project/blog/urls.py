from django.urls import path, re_path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('home/', views.test, name='home')
]