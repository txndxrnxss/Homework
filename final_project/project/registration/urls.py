from django.urls import path, re_path, include
from . import views

app_name = 'registration'
urlpatterns = [
    path('registration/', views.register, name='registration'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]