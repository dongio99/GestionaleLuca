from django.shortcuts import render
from django.http import HttpResponse

def prodotti_view(request, *args, **kwargs):
    return render(request, "index.html", {})