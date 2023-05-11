"""Определение административной панели для моделей Post, Comment и User в Django-приложении blog."""

from django.contrib import admin
from blog.models import  Post, Comment
from django.contrib.auth.models import User


admin.site.unregister(User)
@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
   ...

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...
