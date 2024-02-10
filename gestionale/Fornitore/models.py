from django.db import models
from Pagamento.models import Pagamento
 
class Fornitore(models.Model):
    ragione_sociale = models.CharField(max_length=255)
    indirizzo_sede = models.CharField(max_length=255, blank=True)
    n_civico_sede = models.CharField(max_length=10, blank=True)
    citta_sede = models.CharField(max_length=255, blank=True)
    provincia_sede = models.CharField(max_length=2, blank=True)
    cap_sede = models.CharField(max_length=255, blank=True)
    pagamento = models.ManyToManyField(Pagamento, 
                                  blank=True, 
                                  choices=Pagamento.get_mod_pagamento(),
                                  verbose_name = 'Metodi pagamento possibili')

    @staticmethod
    def getChoices():
        return ((f.ragione_sociale, f.ragione_sociale) for f in Fornitore.objects.all())
    
