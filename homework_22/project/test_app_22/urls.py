from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contacts, name='contact'),
]
