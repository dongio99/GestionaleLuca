from django.contrib import admin
from .models import Movimento, Acquisto, Vendita

admin.site.register(Movimento)
admin.site.register(Acquisto)
admin.site.register(Vendita)
