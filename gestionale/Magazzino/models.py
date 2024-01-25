from django.db import models
from django.forms import ValidationError
from Prodotto.models import Prodotto

def validate_positive(value):
    if value <= 0:
        raise ValidationError("La quantità deve essere maggiore di zero.")


class Magazzino(models.Model):
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    quantita = models.IntegerField(validators=[validate_positive])