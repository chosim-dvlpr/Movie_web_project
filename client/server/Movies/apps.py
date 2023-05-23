from django.apps import AppConfig
from django.conf import settings
import Movies

class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Movies'
    
    def ready(self):
        if settings.SCHEDULER_DEFAULT:
            from . import forapi
            forapi.start()
