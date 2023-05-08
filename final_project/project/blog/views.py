from django.shortcuts import render
from blog.models import User, Post
from django.db.models import Q

def db_get(info_arr):
    info_db_dict = {}
    for i in info_arr:
        info_db_dict[i]= list(Post.objects.filter(title= str(i)).values('title', 'description', 'image'))
    return info_db_dict


def cookies_and_comm(request):
    if 'user_info'not in request.COOKIES:
        get_posts_name = Post.objects.all()
        checker_cookies = False
        return render(request, 'home.html', {'checker_cookies': checker_cookies, 'big_data': db_get(get_posts_name)})
    else:
        get_posts_name = Post.objects.all()
        users_cookies =  request.COOKIES['user_info'].split(' ')
        users_cookies = users_cookies[0]
        checker_cookies = True
        return render(request, 'home.html', {'users_cookies': users_cookies, 'checker_cookies': checker_cookies, 'big_data': db_get(get_posts_name)})