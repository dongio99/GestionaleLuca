from django.apps import AppConfig


class MagazzinoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Magazzino"

    def ready(self):
        import Magazzino.signals
