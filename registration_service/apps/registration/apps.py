from django.apps import AppConfig


class RegistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.registration'


class CoreConfig(AppConfig):
    name = 'registration'
