from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .validator import *
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

# Функция для авторизации пользователя
def user_login(request):

    # Создание формы для ввода логина и пароля
    form = AuthenticationForm()
    if request.method == 'POST':
        # Если данные были отправлены методом POST, то происходит их проверка на валидность
        form = AuthenticationForm(data=request.POST)
       
        if form.is_valid():
            # Получение пользователя, который пытается залогиниться
            user = form.get_user()
            if user.is_authenticated:   
                # Если пользователь авторизован, то происходит его вход в систему
                login(request, user)
                # Перенаправление на главную страницу
                return redirect('http://127.0.0.1:8000/blog/home/')
        else:
            
            return render(request, 'login.html', {'form': form, 'error_log': 'Вы ввели неверный логин или пароль'})
    else:    
        return render(request, 'login.html', {'form': form})


# Функция для разлогирования пользователя
def logout_view(request):
    """
    Представление разлогирования
    """
    # Выход пользователя из системы
    logout(request)

    # Перенаправление на страницу входа в систему
    return redirect('http://127.0.0.1:8000/accounts/login/')




# Функция для регистрации нового пользователя
def register(request):
    if request.method == 'POST':
        # Если данные были отправлены методом POST, то происходит их проверка на валидность
        form = SignUpForm(request.POST)
     
       
        if form.is_valid():
            # Создание нового пользователя на основе данных, введенных в форму
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            # Авторизация пользователя после регистрации
            user = authenticate(username=username, password=password)
            login(request, user)

            # Перенаправление на главную страницу
            return redirect('http://127.0.0.1:8000/blog/home')
        else:
            
            return render(request, 'registration.html', {'form': form, 'error_title':'Введенные данные некорректны!','error_info':'Пароль должен иметь не менее 6 символов буквы и цифры'})
    else:
        # Вывод формы для заполнения при GET-запросе
        form = SignUpForm()
        
    return render(request, 'registration.html', {'form': form})
