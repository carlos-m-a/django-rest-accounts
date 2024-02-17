from django.apps import AppConfig
from . import signals


class ReusableAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        super().ready()
        import signals 