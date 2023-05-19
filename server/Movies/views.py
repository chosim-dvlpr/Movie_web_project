from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie, Review
from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer, ReviewListSerializer



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

#3
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

#4
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

#2
# 특정 영화에 들어가서 댓글을 작성하는 함수.
# 영화정보를 불러오지만(model = Movie), 우리가 생성해야하는 데이터는 리뷰와 관련된 것(serializer의 참조 model = Review).
@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail(request, review_pk):
#     review = get_object_or_404(Review, pk=review_pk)

#     if request.method == 'GET':
#         serializer = ReviewDetailSerializer(review)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = ReviewDetailSerializer(review, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
        
#     elif request.method == 'DELETE':
#         review.delete()
#         data = {
#             'delete': f'review {review_pk} is deleted'
#         }
#         return Response(data, status=status.HTTP_204_NO_CONTENT)




from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class MyTokenObtainPairView(TokenObtainPairView):
    # 커스텀 페이로드 추가
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # 추가 정보를 응답에 포함시킬 수 있음
        response.data['custom_field'] = 'custom_value'
        return response

class MyTokenRefreshView(TokenRefreshView):
    pass
