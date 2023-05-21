import requests
from django.core.management.base import BaseCommand
from Movies.models import Movie
import json

class Command(BaseCommand):
    help = 'Imports data from TMDB API'

    def handle(self, *args, **options):
        # TMDB API에서 데이터 가져오기        
        url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NGY0YTU4NGExZjQ3YThiMWJiODA2ZWJjOTllNGRmNiIsInN1YiI6IjYzZDMxYjY1ZTcyZmU4MDBhYTAyNmNkMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.uiee1bJo9rEkcNKXF4gROV0OEaaqcYp1Cv9vFKkt2mM"
        }

        response = requests.get(url, headers=headers)
        data = response.json()
        
        # 데이터를 fixtures에 저장
        fixtures = []
        for item in data['results']:
            print(item)
            '''
            fixtures.append({
                'model': 'Movies.Movie',
                'fields': {
                    'title': item['title'],
                    'overview': item['overview'],
                    'release_date': item['release_date'],
                    # 필드들을 적절히 매칭
                }
            })

        # fixtures 파일 생성
        with open('Movies/fixtures/tmdb_data.json', 'w') as f:
            f.write(json.dumps(fixtures, indent=4))
        '''