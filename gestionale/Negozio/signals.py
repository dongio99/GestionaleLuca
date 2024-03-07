from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from .models import Negozio


@receiver(post_save, sender=apps.get_model("Prodotti", "Prodotto"))
def initialize_giacenza(sender, instance, created, **kwargs):
    if created:
        Negozio.objects.create(prodotto=instance)
