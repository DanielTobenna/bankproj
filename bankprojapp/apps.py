from django.apps import AppConfig


class BankprojappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bankprojapp'

    def ready(self):
    	import bankprojapp.signals
