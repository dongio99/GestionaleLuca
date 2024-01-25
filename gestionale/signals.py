from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from Magazzino.models import Magazzino
from gestionale import Prodotto

@receiver(pre_delete, sender=Prodotto)
def prevent_deletion(sender, instance, **kwargs):
    if Magazzino.objects.filter(prodotto=instance).exists():
        # Impedisce l'eliminazione del prodotto se è presente nel magazzino
        raise ValidationError("Non puoi eliminare un prodotto presente nel magazzino.")
