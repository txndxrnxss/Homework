from django.urls import path, re_path, include
from . import views

app_name = 'registration'
urlpatterns = [
    path('registration/', views.register, name='registration'),
    path('xxx', views.registration, name='xxx'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout')
] 