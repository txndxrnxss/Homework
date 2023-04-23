from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def skills(request):
    return render(request, 'skills.html')

def education(request):
    return render(request, 'education.html')

def contacts(request):
    return render(request, 'contacts.html')

# base.html - базовое представление всех страниц
# home.html - расширяет шаблон base.html и содержит информацию о вас и ссылки на другие разделы
# skills.html - расширяет шаблон base.html и содержит таблицу hard-skills и soft-skills
# education.html - расширяет шаблон base.html и содержит информацию об образовании
# contacts.html - ссылки на LinkedIn, Facebook, Github и другие социальные сети