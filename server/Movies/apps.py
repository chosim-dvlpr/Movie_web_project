from django.apps import AppConfig

class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Movies'
    
    def ready(self):
        from .models import Movie
        from .views import api_movie

        Movie = Movies.get_model('Movies', 'Movie')
        api_movie()
