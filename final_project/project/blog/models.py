"""Определение моделей в Django-приложении blog."""

from django.db import models 
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class Post(models.Model):

    """
    Класс Post - модель для создания постов блога. Наследуется от базового класса models.Model.
    Атрибуты класса: 
        title - название поста, тип поля CharField. 
        description - описание поста, тип поля CharField.
        image - изображение поста, тип поля ImageField.

    """

    title = models.CharField(max_length = 50, verbose_name = "Post's Title")   
    description = models.CharField(max_length = 1000, verbose_name = "Post's Description")   
    image = models.ImageField(upload_to="static/img/post", blank=True, null=True, verbose_name="Post's Image")   

    def __str__(self):  # метод, который возвращает строковое представление экземпляра класса.
        return f"{self.title}"
    
class Comment(models.Model):

    """
    Класс Comment - модель для создания комментариев к постам блога. Наследуется от базового класса models.Model.
    Атрибуты класса: 
        user - пользователь, который оставил комментарий.
        post - пост, к которому был оставлен комментарий.
        info_comm - текст комментария, тип поля TextField.
        nickname - псевдоним пользователя, тип поля CharField.

    """

    user = models.ForeignKey(User, null = True, blank = True, on_delete = models.SET_DEFAULT, default="")
    post = models.ForeignKey(Post, null = True, blank = True, on_delete = models.SET_DEFAULT, default="")
    info_comm = models.TextField(max_length = 200, verbose_name = "Comment's info", null = True)
    nickname = models.CharField(max_length = 30, verbose_name = "Nickname", null = True)
    
    def __str__(self): # метод, который возвращает строковое представление экземпляра класса.
        return f"{self.info_comm}"