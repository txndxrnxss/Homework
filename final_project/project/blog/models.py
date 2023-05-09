from django.db import models 

class User(models.Model):
    email = models.CharField(max_length = 30, verbose_name = "Email", unique=True)
    login = models.CharField(max_length = 30, verbose_name = "Login", unique=True)
    password = models.CharField(max_length = 30, verbose_name = "Password")
    nickname = models.CharField(max_length = 30, verbose_name = "Nickname")

    def __str__(self):
        return f"{self.login}"

class Post(models.Model):
    title = models.CharField(max_length = 50, verbose_name = "Post's Title")
    description = models.CharField(max_length = 400, verbose_name = "Post's Description")
    image = models.ImageField(upload_to="static/img/post", blank=True, null=True, verbose_name="Post's Image")

    def __str__(self):
        return f"{self.title}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, null = True, blank = True, on_delete = models.SET_DEFAULT, default="")
    post_id = models.ForeignKey(Post, null = True, blank = True, on_delete = models.SET_DEFAULT, default="")
    info_comm = models.TextField(max_length = 200, verbose_name = "Comment's info", null = True)
    # grade = models.IntegerField()
    

    def __str__(self):
        return f"{self.info_comm}"