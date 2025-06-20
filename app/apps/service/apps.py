from django.apps import AppConfig


class ServiceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.service"

    def ready(self):
        import apps.service.signals
