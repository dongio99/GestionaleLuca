from django.shortcuts import render
from django.views import View
from .models import Magazzino
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string


class MagazzinoView(View):
    template_name = "Magazzino/index.html"

    def get(self, request, *args, **kwargs):

        search_codice = request.GET.get("search_codice")
        search_nome = request.GET.get("search_nome")
        operator = request.GET.get("operator")
        search_qnt = request.GET.get("search_qnt")
        query = Q()
        prodotti = Magazzino.objects.filter(quantita__gt=0)

        if search_codice:
            query &= Q(prodotto__codice__icontains=search_codice)
        if search_nome:
            query &= Q(prodotto__nome__icontains=search_nome)
        if search_qnt:
            if operator == 'gt':
                query &= Q(quantita__gt=search_qnt)
            if operator == 'lt':
                query &= Q(quantita__lt=search_qnt)
            if operator == '=':
                query &= Q(quantita=search_qnt)

        prodotti = prodotti.filter(query)
        context = {"giacenze": prodotti}

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            data = dict()
            data["my_content"] = render_to_string(
                "Magazzino/table_content.html", context, request=request
            )
            return JsonResponse(data)
        else:
            return render(request, self.template_name, context)
