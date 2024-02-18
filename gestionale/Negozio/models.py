from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from Prodotto.models import Prodotto
from Iva.models import Iva


class Negozio(models.Model):
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    quantita = models.IntegerField()
    prezzo_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(choices=Iva.getChoices(), max_digits=5, decimal_places=2)
    prezzo_finale = models.DecimalField(max_digits=10, decimal_places=2)
    sconto = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
