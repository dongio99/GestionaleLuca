from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from .models import Magazzino


@receiver(post_save, sender=apps.get_model("Prodotto", "Prodotto"))
def initialize_giacenza(sender, instance, created, **kwargs):
    if created:
        Magazzino.objects.create(prodotto=instance, quantita=0)
