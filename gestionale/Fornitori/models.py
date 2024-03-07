from django.db import models


class Pagamento(models.Model):
    descrizione = models.CharField(max_length=255)

    def __str__(self):
        return self.descrizione


class Fornitore(models.Model):
    ragione_sociale = models.CharField(max_length=255)
    indirizzo_sede = models.CharField(max_length=255, blank=True)
    n_civico_sede = models.CharField(max_length=10, blank=True)
    citta_sede = models.CharField(max_length=255, blank=True)
    provincia_sede = models.CharField(max_length=2, blank=True)
    cap_sede = models.CharField(max_length=255, blank=True)
    pagamento = models.ManyToManyField(
        Pagamento,
        blank=True,
        verbose_name="Metodi pagamento possibili",
    )

    def __str__(self):
        return self.ragione_sociale

    @staticmethod
    def getChoices():
        return [(f.ragione_sociale, f.ragione_sociale) for f in Fornitore.objects.all()]
