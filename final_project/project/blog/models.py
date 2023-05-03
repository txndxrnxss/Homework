from django.db import models 

class User(models.Model):
    login = models.CharField(max_length = 30, verbose_name = "Login")
    password = models.CharField(max_length = 30, verbose_name = "Password")
    nickname = models.CharField(max_length = 30, verbose_name = "Nickname") 

    def __str__(self):
        return f"{self.login}"

class Post(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Post's Title")
    description = models.CharField(max_length = 140, verbose_name = "Post's Description")

    def __str__(self):
        return f"{self.title}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, null = True, blank = True, on_delete = models.SET_DEFAULT, default="")
    post_id = models.ForeignKey(Post, null = True, blank = True, on_delete = models.SET_DEFAULT, default="")
    info_comm = models.TextField(max_length = 200, verbose_name = "Comment's info", null = True)
#     user = models.CharField(max_length = 30, verbose_name = "Game Name")
#     # pub_date = models.DateField(verbose_name = "Add date")
#     # release_date = models.DateField(verbose_name = "Release Time")
#     # price = models.IntegerField(verbose_name = "Price")
#     # slug = models.SlugField(max_length = 20, verbose_name = "Short Game's Name")
#     # category = models.ForeignKey(Category, null = True, blank = True, on_delete = models.SET_DEFAULT, default="")

#     # game_image = models.ImageField(upload_to = "Game", blank = True, null = True, verbose_name = "Game's Image")
#     # is_active = models.BooleanField(verbose_name = "Game is active?")

    def __str__(self):
        return f"{self.info_comm}"