from django.shortcuts import render
from blog.models import User

def test(request):
    if 'user_info'not in request.COOKIES:
        checker_cookies = False
        return render(request, 'home.html', {'checker_cookies': checker_cookies})
    else:
        users_cookies =  request.COOKIES['user_info'].split(' ')
        users_cookies = users_cookies[0]
        checker_cookies = True
        return render(request, 'home.html', {'users_cookies': users_cookies, 'checker_cookies': checker_cookies})
    

