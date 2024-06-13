from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from Prodotti.models import Prodotto
from Iva.models import Iva


class Negozio(models.Model):
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    quantita = models.IntegerField(default=0.00)
    imponibile_non_scontato = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    iva = models.DecimalField(max_digits=5, decimal_places=2, default=22.00)
    prezzo_finale_non_scontato = models.DecimalField(max_digits=10, decimal_places=2,  default=0.00, editable=False)
    sconto = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    prezzo_finale_scontato = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_iva_choices()

    def _set_iva_choices(self):
        self._meta.get_field('iva').choices = Iva.getChoices()
    
    def save(self, *args, **kwarg) -> None:
        self.prezzo_finale = self.imponibile_non_scontato * (1 + self.iva / 100)
        self.prezzo_finale_scontato = self.imponibile_non_scontato * (1 + self.iva / 100) * (1 - self.sconto / 100)
        return super().save()