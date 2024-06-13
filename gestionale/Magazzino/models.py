from django.db import models
from django.forms import ValidationError
from Prodotti.models import Prodotto
from django.core.validators import MinValueValidator


class Magazzino(models.Model):
    prodotto = models.ForeignKey(Prodotto, on_delete=models.CASCADE)
    quantita = models.IntegerField(validators=[MinValueValidator(0)])

    def createGiacenza(id_prodotto):
        Magazzino.objects.create(prodotto=id_prodotto, quantita=0)

    # def updateQnt(quantita, movimento):
    #    gicenza = new Magazzino()

    class Meta:
        db_table = "magazzino"