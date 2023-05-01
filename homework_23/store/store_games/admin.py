from django.contrib import admin
from .models import Game, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'description', 'is_active', 'game_amount')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'pub_date', 'release_date', 'price', 'category', 'description', 'is_active')
