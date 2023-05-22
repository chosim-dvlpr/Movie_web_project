import requests
from ..data import API_KEY
from .models import Movie

url = f"https://api.themoviedb.org/3/movie/popular?language=ko&page=1&api_key={API_KEY}"

response = requests.get(url).json()
movie_data = response.get['results']
# data = []

for movie in movie_data:
    Movie.objects.create({
        'adult': movie.get('adult'),
        'backdrop_path': movie.get('backdrop_path'),
        'genre_ids': movie.get('genre_ids'),
        'id': movie.get('id'),
        'original_language': movie.get('original_language'),
        'original_title': movie.get('original_title'),
        'overview': movie.get('overview'),
        'popularity': movie.get('popularity'),
        'poster_path': movie.get('poster_path'),
        'release_date': movie.get('release_date'),
        'title': movie.get('title'),
        'video': movie.get('video'),
        'vote_average': movie.get('vote_average'),
        'vote_count': movie.get('vote_count'),
    })

