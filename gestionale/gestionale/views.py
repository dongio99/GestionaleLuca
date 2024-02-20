from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, F
from Prodotto.models import Prodotto, Categoria
from Movimenti.models import Acquisto, Vendita
from django.utils.formats import date_format

import json

from Negozio.models import Negozio
from django.views import View


def dati_grafico_view(request):
    dati_acquisto = get_dati_movimenti(Acquisto)
    dati_vendita = get_dati_movimenti(Vendita)
    dati_grafico = {"acquisto": dati_acquisto, "vendita": dati_vendita}
    return JsonResponse(dati_grafico)


def get_dati_movimenti(tipo_movimento):
    mesi_importo = {
        "Gennaio": 0,
        "Febbraio": 0,
        "Marzo": 0,
        "Aprile": 0,
        "Maggio": 0,
        "Giugno": 0,
        "Luglio": 0,
        "Agosto": 0,
        "Settembre": 0,
        "Ottobre": 0,
        "Novembre": 0,
        "Dicembre": 0,
    }

    dati_movimenti = tipo_movimento.get_movimenti_by_year(datetime.now().year)

    # Aggiorna i valori effettivi dei mesi con i dati disponibili
    for movimento in dati_movimenti:
        mese = date_format(movimento.data, "F")
        mesi_importo[mese] += float(movimento.prezzo_finale)

    # Restituisci i dati formattati per il grafico
    return [
        {"label": mese, "y": float(prezzo)} for mese, prezzo in mesi_importo.items()
    ]


class DashboardView(View):
    template_name = "Dashboard/dashboard.html"

    def get(self, request, *args, **kwargs):
        prodotti = (
            Prodotto.objects.filter(soglia_riordino__gt=-1)
            .annotate(
                total_quantita=Sum("negozio__quantita") + Sum("magazzino__quantita")
            )
            .filter(total_quantita__lt=F("soglia_riordino"))
        )
        context = {"anno": datetime.now().year, "prodotti": prodotti}
        return render(request, self.template_name, context)
