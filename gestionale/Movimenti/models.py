from decimal import Decimal
from django.db import models
from Prodotto.models import Prodotto
from Fornitore.models import Fornitore
from Iva.models import Iva
from Magazzino.models import Magazzino


class Movimento(models.Model):
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    codice_prodotto = models.CharField(default=None, max_length=255)
    quantita = models.IntegerField()
    imponibile_unitario = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    prezzo_unitario = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False, default=0.00
    )
    iva = models.DecimalField(choices=Iva.getChoices(), max_digits=5, decimal_places=2)
    prezzo_finale = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False, default=0.00
    )
    # data = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.prezzo_unitario = ((1 + self.iva) / 100) * self.imponibile_unitario
        self.prezzo_finale = self.quantita * self.prezzo_unitario
        self.codice_prodotto = self.prodotto.codice
        super().save(*args, **kwargs)


class Acquisto(Movimento):
    fornitore = models.CharField(max_length=255, choices=Fornitore.getChoices())


# class Vendita(Movimento):


class Trasferimento(Movimento):
    ORIGINE_CHOICES = [
        ("MAGAZZINO", "Magazzino"),
        ("NEGOZIO", "Negozio"),
    ]
    origine = models.CharField(max_length=20, choices=ORIGINE_CHOICES)
    destinazione = models.CharField(max_length=20, editable=False)

    def save(self, *args, **kwargs):
        if self.origine == "MAGAZZINO":
            self.destinazione = "NEGOZIO"
        elif self.origine == "NEGOZIO":
            self.destinazione = "MAGAZZINO"
        super().save(*args, **kwargs)
