from decimal import Decimal
from functools import cached_property
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

    @classmethod
    def getChoices(cls) -> list[tuple[Decimal, str]]:
        return [(iva.percentuale, f"{iva.percentuale}%") for iva in cls.objects.all()]