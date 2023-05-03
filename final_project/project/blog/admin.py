from django.contrib import admin
from blog.models import User, Post, Comment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ...