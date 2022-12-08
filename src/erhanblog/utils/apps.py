from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "erhanblog.utils"

    def ready(self):
        from . import checks  # noqa
