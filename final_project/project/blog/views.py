from django.shortcuts import render
from blog.models import User

def test(request):
    form = 3
    data = User.objects.filter(login = 'txndxrnxss').values('password')
    print(data)
    return render(request, 'home.html', {'form': form})