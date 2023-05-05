from django.db import models


class InfoInMixin(models.Model):
    slug = models.SlugField(max_length=20, verbose_name="Short name category")
    is_active = models.BooleanField()

    class Meta:
        abstract = True


class Category(InfoInMixin):
    title = models.CharField(max_length = 50, verbose_name = "Category Title")
    description = models.CharField(max_length = 140, verbose_name = "Category's Description")
    game_amount = models.IntegerField(default=0)

    @classmethod
    def default_category(cls):
        category, created = cls.objects.get_or_create(
            title='default',
            slug='default',
            description='default description',
            is_active=True
        )
        return category.pk

    def __str__(self):
        return f'{self.title}'
    
class Game(InfoInMixin):
    name = models.CharField(max_length = 30, verbose_name = "Game Name")
    pub_date = models.DateField(verbose_name = "Add date")
    release_date = models.DateField(verbose_name = "Release Time")
    price = models.IntegerField(verbose_name = "Price")
    category = models.ForeignKey(Category, null = True, blank = True, on_delete = models.SET_DEFAULT, default=Category.default_category)
    description = models.TextField(verbose_name = "Game's Description")
    game_image = models.ImageField(upload_to = "Game", blank = True, null = True, verbose_name = "Game's Image")

    class Meta:
        verbose_name = "Game"
        verbose_name_plural = "Games"

    def __str__(self):
        return f"{self.name}"

