from django.apps import AppConfig


class GamemodelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gamemodels'

    def ready(self):
        import gamemodels.signals
