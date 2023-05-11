"""Настройка маршрутизации URL для Django-приложения blog."""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    # При переходе на '/blog/' происходит маршрутизация на файл urls.py из Django-приложения blog.
    path('blog/', include('blog.urls')),

    # При переходе на '/accounts/' происходит маршрутизация на файл urls.py из приложения registration.
    path('accounts/', include('registration.urls')),

    # При переходе на '/admin/' происходит перенаправление на стандартный интерфейс администратора Django.
    path('admin/', admin.site.urls)
    
]
