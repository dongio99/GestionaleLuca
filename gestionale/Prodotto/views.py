from django.shortcuts import render
from django.db.models import Q
from django.http import JsonResponse
from .models import Prodotto, Categoria
from django.views import View
from django.template.loader import render_to_string

class ProdottiView(View):
    template_name = "index.html"
    template_name_table = "table_content.html"

    def get(self, request, codice_cat=None, *args, **kwargs):
        codice_cat_get = request.GET.get('codice_cat_get')
        if codice_cat == None:
            codice_cat = codice_cat_get
        search_codice = request.GET.get('search_codice')
        search_nome = request.GET.get('search_nome')
        search_cat = request.GET.get('search_cat')
        query = Q()
        prodotti = Prodotto.objects.all()

        if codice_cat :
            cat = Categoria.objects.get(nome=codice_cat)
            query &= Q(id_categoria=cat.id)
        if search_codice:
            query &= Q(codice__icontains=search_codice)
        if search_nome:
            query &= Q(nome__icontains=search_nome)
        if search_cat:
            query &= Q(id_categoria__nome__icontains=search_cat)
        
        prodotti = prodotti.filter(query)
        prodotti = prodotti.distinct()

        context = {"prodotti": prodotti}
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            data = dict()
            context = {"prodotti": prodotti}
            data['my_content'] = render_to_string("table_content.html", context, request=request)
            return JsonResponse(data)
        else:
            return render(request, self.template_name, context)