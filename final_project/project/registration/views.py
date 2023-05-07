from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from .forms import LoginForm
from .validator import *
from blog.models import User, Comment
from django.db import IntegrityError
from django.db.models import Q

def register(request):
    if 'user_info' in request.COOKIES:
        return redirect('http://127.0.0.1:8000/accounts/xxx')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            login = request.POST['login']
            password = request.POST['password']
            nickname = request.POST['nickname']
            check_valid = Validator(login, password, email).validate()
            if check_valid == True:
                check_email = User.objects.filter(email=email).first()
                check_login = User.objects.filter(login=login).first() 
                if not check_email and not check_login:
                    user = User(email=email, login=login, password=password, nickname=nickname)
                    user.save()
                    response = redirect('http://127.0.0.1:8000/blog/home/')
                    response.set_cookie('user_info' , login + ' ' + password + ' ' + email)
                    return response
                else:
                    return render(request, 'registration.html', {'error_info': 'Пользователь с такой почтой или логином уже существует!'})
            else:
                return render(request, 'registration.html', context={'check_valid': check_valid})
        else:
            return render(request, 'registration.html')



def registration(request):
    if 'user_info'not in request.COOKIES:
        return redirect('http://127.0.0.1:8000/accounts/registration/')
    else:
        return render(request, 'base_rg.html', {'form': request.COOKIES['user_info']})



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        users = User.objects.filter(Q(email=email) & Q(password=password))
        
        print(users)
        if users != []:
            username = users.first().login
            response = redirect('http://127.0.0.1:8000/blog/home/')
            response.set_cookie('user_info' , str(username) + ' ' + password + ' ' + email)
            return response
    else:
        if 'user_info'not in request.COOKIES:
            return render(request, 'login.html')
        else:
            return render(request, 'home.html')
    


def logout_view(request):
    """
    Представление разлогирования
    """
    response = HttpResponseRedirect('http://127.0.0.1:8000/blog/home/')
    response.delete_cookie('user_info')
    return response 