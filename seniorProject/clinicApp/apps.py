from django.apps import AppConfig


class ClinicappConfig(AppConfig):
    name = 'clinicApp'

    def ready(self):
        from .scheduler import updater
        updater.start()
