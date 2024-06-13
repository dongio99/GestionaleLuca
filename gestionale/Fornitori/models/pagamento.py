from django.db import models

class Pagamento(models.Model):
    descrizione = models.CharField(max_length=255)

    def __str__(self):
        return self.descrizione
    
    class Meta:
        db_table = "pagamenti"
