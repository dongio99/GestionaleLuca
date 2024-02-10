from django.shortcuts import render
from .models import Prodotto, Categoria
from django.views import View

class ProdottiView(View):
    template_name = 'index.html'

    def get(self, request, codice_cat=None, *args, **kwargs):
        if codice_cat:
            cat = Categoria.objects.get(nome=codice_cat)
            prodotti = Prodotto.objects.filter(id_categoria=cat.id)
        else:
            prodotti = Prodotto.objects.all()
        
        context = {'prodotti': prodotti}
        return render(request, self.template_name, context)