from django.db import models

class Prodotto(models.Model):
    codice = models.CharField(max_length=255, unique=True)
    nome = models.CharField(max_length=255)
    produttore = models.CharField(max_length=255, blank=True)
    soglia_riordino = models.IntegerField(default=-1)
    categoria = models.CharField(max_length=255, blank=True)
