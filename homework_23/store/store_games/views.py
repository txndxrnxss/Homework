from django.shortcuts import render, get_object_or_404
from store_games.models import *
from django.http import HttpResponse, HttpRequest

def home(request: HttpRequest):
    db_dict = Game.objects.order_by('name')
    return render(request,'home.html', {'games': db_dict})
    

def home_sort(request: HttpRequest, sort):
    sort_order = {
        'None': Game.objects.all(),
        'price': Game.objects.order_by('price'),
        'name': Game.objects.order_by('name'),
    }
    games = sort_order.get(sort).all()
    categories = list(Category.objects.all())
    return render(request, 'home.html', context={'games': games, "categories": categories})

def game_name(request: HttpRequest, game):
    print(game)
    data = Game.objects.filter(name= str(game)).values('name','category', 'description', 'price', 'pub_date', 'release_date')
    return render(request,'base.html', {'objects': data})


def category_id(request: HttpRequest, category):
    if category == 'Хорроры':
        id = 2
    else:
        id = 1
    data = Category.objects.filter(title= str(category)).values('title', 'description')
    ct_games = Game.objects.filter(category= str(id)).values('name')
    return render(request, 'categories.html', {'objects': data, 'ctg': ct_games})
