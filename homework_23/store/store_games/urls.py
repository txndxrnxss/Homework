from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  
    path('home/<sort>', views.home_sort, name='sort'),  # сортировка по name или price
    path('home/game/<game>', views.game_name, name='game'),  
    path('home/category/<category>', views.category_id, name='category')
]