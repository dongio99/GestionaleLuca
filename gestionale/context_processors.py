from Prodotto.models import Categoria 

def categorie_prodotti(request):
    categorie = Categoria.getDistinctLabel()
    return {'categorie_prodotti': categorie}