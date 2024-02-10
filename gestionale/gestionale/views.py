from django.shortcuts import render
from django.db.models import Sum
from Prodotto.models import Prodotto, Categoria

# from Movimenti.models import Acquisto, Vendita
# from Negozio.models import Negozio
from django.views import View


class DashboardView(View):
    template_name = "dashboard.html"

    def get(self, request, *args, **kwargs):
        # prodotti_negozio = Negozio.objects()
        # fatturato = Vendita.objects.annotate(ingresso=Sum("prezzo_finale")) - Acquisto.objects.annotate(uscite=Sum("prezzo_finale"))
        return render(request, self.template_name)
