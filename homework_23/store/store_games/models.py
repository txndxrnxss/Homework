from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Category(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Category Title")
    slug =  models.SlugField(max_length = 20, verbose_name = "Short Category's Name")
    description = models.CharField(max_length = 140, verbose_name = "Category's Description")
    is_active = models.BooleanField(verbose_name = "Category is active?")

    def __str__(self):
        return f'{self.title}'
    
class Game(models.Model):
    name = models.CharField(max_length = 30, verbose_name = "Game Name")
    pub_date = models.DateField(verbose_name = "Add date")
    release_date = models.DateField(verbose_name = "Release Time")
    price = models.IntegerField(verbose_name = "Price")
    slug = models.SlugField(max_length = 20, verbose_name = "Short Game's Name")
    category = models.ForeignKey(Category, null = True, blank = True, on_delete = models.SET_DEFAULT, default="")
    description = models.TextField(verbose_name = "Game's Description")
    game_image = models.ImageField(upload_to = "Game", blank = True, null = True, verbose_name = "Game's Image")
    is_active = models.BooleanField(verbose_name = "Game is active?")

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"

    def __str__(self):
        return f"{self.name}"

