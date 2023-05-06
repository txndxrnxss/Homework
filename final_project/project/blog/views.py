from django.shortcuts import render
from blog.models import User

def test(request):
    return render(request, 'home.html')