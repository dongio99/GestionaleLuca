from django.db import models


class Pagamento(models.Model):
    descrizione = models.CharField(max_length=255)

    @staticmethod
    def get_mod_pagamento():
        return [(p.id, p.descrizione) for p in Pagamento.objects.all()]
