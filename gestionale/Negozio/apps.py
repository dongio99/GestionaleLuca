from django.apps import AppConfig

class NegozioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Negozio"

    def ready(self):
        import Negozio.signals