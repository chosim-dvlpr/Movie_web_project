from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.http.response import JsonResponse

from .models import Movie, Review, Comment, Similarmovie
from .serializers import MovieListSerializer, MovieSerializer, ReviewListSerializer, ReviewSerializer, CommentSerializer, SimilarMovieSerializer

import requests
from .data import API_KEY
from .models import Movie


def start_function():
    print('hello world!')
    for i in range(1, 4):
        url = f"https://api.themoviedb.org/3/movie/popular?language=ko&page={i}&without_genres=10749&api_key={API_KEY}"
        # url = f"https://api.themoviedb.org/3/movie/popular?language=ko&page={i}&without_genres=10749&api_key={API_KEY}"
        print('letsgo')
        response = requests.get(url).json()
        movie_data = response['results']
        # data = []

        for movie in movie_data:
            mv=Movie(title=movie['title'],
                backdrop_path=movie['backdrop_path'],
                poster_path=movie['poster_path'],
                original_language=movie['original_language'],
                original_title=movie['original_title'],
                overview=movie['overview'],
                release_date=movie['release_date'],
                vote_average=movie['vote_average'],
                id=movie['id']
                )
            mv.save()


## 추천 영화 API URL 통해서 데이터 불러오기
def similar_movie_api(request, movie_id):
    print('hello world!')
    for i in range(1, 4):
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/similar?language=ko&page={i}&api_key={API_KEY}"
        # url = f"https://api.themoviedb.org/3/movie/popular?language=ko&page={i}&without_genres=10749&api_key={API_KEY}"
        print('letsgo')
        response = requests.get(url).json()
        movie_data = response['results']
        # data = []

        for movie in movie_data:
            mv=Movie(title=movie['title'],
                poster_path=movie['poster_path'],
                original_language=movie['original_language'],
                original_title=movie['original_title'],
                overview=movie['overview'],
                release_date=movie['release_date'],
                vote_average=movie['vote_average'],
                id=movie['id']
                )
            mv.save()
            mv.movie.add(movie_id)


# @authentication_classes([TokenAuthentication])
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

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


@authentication_classes([TokenAuthentication])
@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


# 전체 리뷰를 조회하는 함수
# ReviewListSerializer 사용
@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save(movie=movie, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # print(serializer.errors)
        
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'review {review_pk} is deleted'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# 리뷰 댓글 작성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = review.user
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def comment_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    print('실행')
    if request.method == 'DELETE':
        comment.delete()
        return Response({ 'id': comment_pk }, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def comment_list(request, review_pk):
    if request.method == 'GET':
        comments = Comment.objects.filter(review_id=review_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
#     if request.method == 'DELETE':

# @api_view(['PUT', 'DELETE'])
# def comment_update_delete(request, comment_pk):
#     comment = get_object_or_404(Comment, pk=comment_pk)
#     if comment.user != request.user:
#         return Response({'detail': '권한없음'}, status=status.HTTP_403_FORBIDDEN)
#     if request.method == 'PUT':
#         serializer = CommentSerializer(comment, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#     else:
#         comment.delete()
#         return Response({'id': comment_pk}, status=status.HTTP_204_NO_CONTENT)


# 영화 좋아요
@api_view(['POST'])
def movie_like(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    user = request.user
    if movie.like_users.filter(id=user.id).exists():
        movie.like_users.remove(user)
        is_like = False
    else:
        movie.like_users.add(user)
        is_like = True
    response = { 
        'isLike': is_like, 
        'likeCount': movie.like_users.count() }
    return JsonResponse(response)


## 추천 영화

# @api_view(['GET'])
# def similar_movie_list(request, movie_id):
#     if request.method == 'GET':
#         similarmovies = Movie.similar_movie.get(id=movie_id)
#         # print(Movie.similar_movie.all())
#         print('*'*100)
#         serializer = SimilarMovieSerializer(similarmovies, many=True)
#         similar_movie_api(request, movie_id)
#         return Response(serializer.data)

@api_view(['GET'])
def similar_movie_list(request, movie_id):
    if request.method == 'GET':
        print('*'*100)
        similarmovies = Similarmovie.objects.get(id=movie_id)
        serializer = SimilarMovieSerializer(similarmovies)
        return Response(serializer.data)
