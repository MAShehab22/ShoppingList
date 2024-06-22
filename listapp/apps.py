from django.apps import AppConfig


class ListappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'listapp'

    def ready(self):
        from . import tasks
        tasks.start_scheduler()
