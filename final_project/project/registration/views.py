from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from .forms import LoginForm
# import requests


def register(request):
    """
    Представлении регистрации
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
        # form.save()
            nickname = form.cleaned_data.get('nickname')
            login = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            print(nickname, login, password)
            messages.success(request, f'Создан аккаунт {nickname}!')
            return redirect(reverse('shop:index'))
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    """
    Представление входа в аккаунт, а также перенаправление.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        next_url = request.POST.get('next') # необходимо для перенаправление на ресурс
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(nickname=cd['nickname'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(next_url)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """
    Представление разлогирования
    """
    logout(request)
    return redirect('http://127.0.0.1:8000/accounts/login/')