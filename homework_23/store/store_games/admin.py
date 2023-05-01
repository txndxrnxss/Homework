from django.contrib import admin

from store_games.models import Category, Game

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    ...
