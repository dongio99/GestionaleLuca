from django.utils import timezone
from decimal import Decimal
from django.db import models
from Prodotti.models import Prodotto
from Fornitori.models import Fornitore
from Iva.models import Iva
from Magazzino.models import Magazzino


class Movimento(models.Model):
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    codice_prodotto = models.CharField(default=None, max_length=255, editable=False)
    quantita = models.IntegerField()
    imponibile_unitario = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    prezzo_unitario = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False, default=0.00
    )
    iva = models.DecimalField(max_digits=5, decimal_places=2)
    

    prezzo_finale = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False, default=0.00
    )
    data = models.DateTimeField(default=timezone.now)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_iva_choices()

    def _set_iva_choices(self):
        self._meta.get_field('iva').choices = Iva.getChoices()

    def save(self, *args, **kwargs):
        self.prezzo_unitario = ((1 + self.iva) / 100) * self.imponibile_unitario
        self.prezzo_finale = self.quantita * self.prezzo_unitario
        self.codice_prodotto = self.prodotto.codice
        super().save(*args, **kwargs)

    @classmethod
    def get_movimenti_by_year(cls, year):
        return cls.objects.filter(data__year=year)


class Acquisto(Movimento):
    id_fornitore = models.ForeignKey(Fornitore, on_delete=models.CASCADE)
    fornitore_rag_soc = models.CharField(max_length=255, editable=False, default="")

    def save(self, *args, **kwargs):
        self.fornitore_rag_soc = self.id_fornitore.ragione_sociale
        super().save(*args, **kwargs)
        
    class Meta:
        db_table = "acquisti"


class Vendita(Movimento):
    
    class Meta:
        db_table = "vendite"



class Trasferimento(Movimento):
    ORIGINE_CHOICES = [
        ("MAGAZZINO", "Magazzino"),
        ("NEGOZIO", "Negozio"),
    ]
    origine = models.CharField(max_length=20, choices=ORIGINE_CHOICES)
    destinazione = models.CharField(max_length=20, editable=False)
    prezzo_unitario = 0
    prezzo_finale = 0
    iva = 0

    def save(self, *args, **kwargs) -> None:
        if self.origine == "MAGAZZINO":
            self.destinazione = "NEGOZIO"
        elif self.origine == "NEGOZIO":
            self.destinazione = "MAGAZZINO"
        super().save(*args, **kwargs)
        
    class Meta:
        db_table = "trasferimenti"
