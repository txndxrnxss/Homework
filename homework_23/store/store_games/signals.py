from django.db.models import signals
from django.dispatch import receiver
from .models import Game, Category

@receiver(signals.post_save, sender=Game)
def update_category_game_amount(sender, instance, created, **kwargs):
    """Уменьшает счетчик поля game_amount на единицу при добавлении игры"""

    category_instance = instance.category

    if created:
        category_instance.game_amount = category_instance.game_amount + 1
    category_instance.save()


@receiver(signals.pre_delete, sender=Game)
def update_category_game_amount_delete(sender, instance, **kwargs):
    """
    Уменьшает счетчик поля game_amount на единицу при удалении игры
    """
    category_instance = instance.category
    category_instance.game_amount -= 1
    category_instance.save()