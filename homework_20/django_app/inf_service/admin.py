from django.contrib import admin

# Register your models here.

from django.contrib import admin
from inf_service.models import User, Post, Category
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
