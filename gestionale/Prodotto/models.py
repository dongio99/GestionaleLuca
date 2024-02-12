from django.db import models

from django.forms import ModelChoiceField

class Categoria(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.nome = self.nome.capitalize()
        super().save(*args, **kwargs)

    @staticmethod
    def getDistinctLabel():
        categorie = Categoria.objects.values("nome").distinct()
        return [categoria["nome"] for categoria in categorie]

    def delete(self, *args, **kwargs):
        prodotti = Prodotto.objects.filter(id_categoria=self.id)
        for prodotto in prodotti:
            prodotto.id_categoria = None
            prodotto.save()

        super().delete(*args, **kwargs)

    def __str__(self):
        return self.nome


class Prodotto(models.Model):
    codice = models.CharField(max_length=255, unique=True)
    nome = models.CharField(max_length=255)
    produttore = models.CharField(max_length=255, blank=True)
    soglia_riordino = models.IntegerField(default=-1)
    id_categoria = models.ManyToManyField(Categoria, default=None)

    def __str__(self):
        return self.nome + " - " + self.codice

    @staticmethod
    def get_categorie_choices():
        return [(categoria.id, categoria.nome) for categoria in Categoria.objects.all()]

    def id_categoria_choices(self):
        return ModelChoiceField(queryset=Categoria.objects.all(), required=False)
