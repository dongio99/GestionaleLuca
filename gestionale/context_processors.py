from Prodotto.models import Prodotto 

def categorie_prodotti(request):
    categorie = Prodotto.getDistinctCategorieListLabel()
    return {'categorie_prodotti': categorie}