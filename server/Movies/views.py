from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from .models import Movie, Review
from .serializers import MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer

import requests
from .data import API_KEY
from .models import Movie


def start_function():
    print('hello world!')
    for i in range(1, 4):
        url = f"https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={i}&without_genres=10749&api_key={API_KEY}"
        print('letsgo')
        response = requests.get(url).json()
        movie_data = response['results']
        # data = []

        for movie in movie_data:
            mv=Movie(title=movie['title'],
                backdrop_path=movie['backdrop_path'],
                original_language=movie['original_language'],
                original_title=movie['original_title'],
                overview=movie['overview'],
                release_date=movie['release_date'],
                vote_average=movie['vote_average'],
                id=movie['id']
                )
            mv.save()
        # Movie.objects.create({
        #     'adult': movie.get('adult'),
        #     'backdrop_path': movie.get('backdrop_path'),
        #     'genre_ids': movie.get('genre_ids'),
        #     'id': movie.get('id'),
        #     'original_language': movie.get('original_language'),
        #     'original_title': movie.get('original_title'),
        #     'overview': movie.get('overview'),
        #     'popularity': movie.get('popularity'),
        #     'poster_path': movie.get('poster_path'),
        #     'release_date': movie.get('release_date'),
        #     'title': movie.get('title'),
        #     'video': movie.get('video'),
        #     'vote_average': movie.get('vote_average'),
        #     'vote_count': movie.get('vote_count'),
        # })






# def api_movie():
#     print('*********************')
#     url = f"https://api.themoviedb.org/3/movie/popular?language=ko&page=1&api_key={API_KEY}"

#     response = requests.get(url).json()
#     movie_data = response.get('results')
#     # data = []

#     # Movie = Movies.get_model('Movies', 'Movie')

#     for movie in movie_data:
#         Movie.objects.create({
#             'adult': movie.get('adult'),
#             'backdrop_path': movie.get('backdrop_path'),
#             # 'genre_ids': movie.get('genre_ids'),
#             # 'id': movie.get('id'),
#             'original_language': movie.get('original_language'),
#             'original_title': movie.get('original_title'),
#             'overview': movie.get('overview'),
#             'popularity': movie.get('popularity'),
#             'poster_path': movie.get('poster_path'),
#             'release_date': movie.get('release_date'),
#             'title': movie.get('title'),
#             'video': movie.get('video'),
#             'vote_average': movie.get('vote_average'),
#             'vote_count': movie.get('vote_count'),
#         })


#3
# @authentication_classes([TokenAuthentication])
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

# import requests
# import json

# Create your views here.

# @api_view(['GET'])
# def actor_list(request):
#     actors = get_list_or_404(Actor)
#     serializer = ActorListSerializer(actors, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def actor_detail(request, actor_pk):
#     actor = get_object_or_404(Actor, pk=actor_pk)
#     serializer = ActorSerializer(actor)
#     return Response(serializer.data)



#4
@authentication_classes([TokenAuthentication])
@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

# 1
# 전체 리뷰를 조회하는 함수
# ReviewListSerializer 사용
@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

# #2
# # 특정 영화에 들어가서 댓글을 작성하는 함수.
# # 영화정보를 불러오지만(model = Movie), 우리가 생성해야하는 데이터는 리뷰와 관련된 것(serializer의 참조 model = Review).
@api_view(['POST'])
def review_create(request, movie_pk):
    # print('나는 일을 한다')
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            print(request.user)
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            print('받음')   
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        
    elif request.method == 'DELETE':
        print('delete')
        review.delete()
        data = {
            'delete': f'review {review_pk} is deleted'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)




