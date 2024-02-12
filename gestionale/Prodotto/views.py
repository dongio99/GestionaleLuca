from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from .models import Prodotto, Categoria
from django.views import View
from django.template.loader import render_to_string

class ProdottiView(View):
    template_name = "index.html"

    def get(self, request, codice_cat=None, *args, **kwargs):
        search_codice = request.GET.get('search_codice')
        search_nome = request.GET.get('search_nome')
        search_cat = request.GET.get('search_cat')
        query = Q()
        prodotti = Prodotto.objects.all()

        if codice_cat:
            cat = Categoria.objects.get(nome=codice_cat)
            query &= Q(id_categoria=cat.id)
        elif search_codice:
            query &= Q(codice__icontains=search_codice)
        elif search_nome:
            query &= Q(nome__icontains=search_nome)
        elif search_cat:
            query &= Q(id_categoria__nome__icontains=search_cat)
        
        prodotti = prodotti.filter(query)
        print(prodotti.query)    

        context = {"prodotti": prodotti}
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Costruisci una lista di dizionari per i dati dei prodotti
            data = [{'codice': prodotto.codice, 'nome': prodotto.nome, 'categoria': prodotto.id_categoria.all()} for prodotto in prodotti]
            return JsonResponse({'data': data})
        else:
            return render(request, self.template_name, context)