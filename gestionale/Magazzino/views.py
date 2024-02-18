from django.shortcuts import render
from django.views import View
from .models import Magazzino


class MagazzinoView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        prodotti = Magazzino.objects.filter(quantita__gt=0)
        context = {"giacenza": prodotti}
        return render(request, self.template_name, context)
