from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Iva(models.Model):
    percentuale = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    def __str__(self) -> str:
        return str(self.percentuale)

    @staticmethod
    def getChoices() -> list[tuple[Decimal, str]]:
        return [(iva.percentuale, f"{iva.percentuale}%") for iva in Iva.objects.all()]
