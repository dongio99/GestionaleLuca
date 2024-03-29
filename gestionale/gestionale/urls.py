"""
URL configuration for gestionale project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path
from Prodotti.views import ProdottiView, CreateProduct
from Magazzino.views import MagazzinoView
from .views import DashboardView, dati_grafico_view

urlpatterns = [
    path("prodotti/", ProdottiView.as_view(), name="prodotti_tutti"),
    path("prodotti/", ProdottiView.as_view(), name="update_table_prodotti"),
    path("prodotti/", CreateProduct.as_view(), name="crea_prodotto"),
    path(
        "prodotti/<str:codice_cat>/", ProdottiView.as_view(), name="prodotti_categoria"
    ),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("", RedirectView.as_view(url="/dashboard/"), name="index"),
    path("dati_grafico/", dati_grafico_view, name="dati_grafico"),
    path("magazzino/", MagazzinoView.as_view(), name="magazzino"),
    path("magazzino/", MagazzinoView.as_view(), name="update_table_magazzino"),
    path("admin/", admin.site.urls),
]
