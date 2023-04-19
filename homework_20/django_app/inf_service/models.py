# from django.db import models
# # Create your models here.

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    # login = models.TextField(validators=[validate_login])
    # email = models.TextField(validators=[validate_email]) 
    register = models.TextField(max_length=10)

    def __str__(self):
        return f"Имя:{self.first_name}/Фамилия:{self.last_name}"

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_title = models.TextField()

    def __str__(self):
        return f"Название: {self.category_title}"

class Post(models.Model):
    title = models.TextField()
    data_created = models.TextField(max_length=10)
    content = models.TextField(max_length=140)
    post_author_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    post_category_id = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL) 

    def __str__(self):
        return f"Название:{self.title}/Дата создания: {self.data_created}/{self.post_category_id}"