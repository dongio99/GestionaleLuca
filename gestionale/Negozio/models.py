from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from Prodotto.models import Prodotto
from Iva.models import Iva


class Negozio(models.Model):
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    quantita = models.IntegerField()
    imponibile_non_scontato = models.DecimalField(max_digits=10, decimal_places=2)
    iva = models.DecimalField(choices=Iva.getChoices(), max_digits=5, decimal_places=2)
    prezzo_finale_non_scontato = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    sconto = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    prezzo_finale_scontato = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self) -> None:
        self.prezzo_finale = self.imponibile * (1 + self.iva / 100)
        self.prezzo_finale_scontato = self.imponibile * (1 + self.iva / 100) * (1 - self.sconto / 100)
        return super().save()