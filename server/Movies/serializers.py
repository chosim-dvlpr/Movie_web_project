from rest_framework import serializers
# from .models import Actor, Movie, Review
from .models import Movie, Review, Comment
from django.contrib.auth import get_user_model
from Accounts.serializers import UserSerializer

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields= '__all__'

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        # fields = ('id', 'title', 'content',)
        fields = '__all__'

        read_only_fields = ('id','movie',)


class ReviewSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = '__all__'

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'

    user = UserSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        # read_only_fields = ('id','movie',)



class CommentSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('content','user', 'id',)

## 추천영화

from .models import Similarmovie

class SimilarMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Similarmovie
        fields = ('title',)

# 첫 번째 방법
# class MovieTitleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('title',)

# 두 번째 방법 - views에서 사용하지 않는 class를 다른 class와 통합하기
# class ActorSerializer(serializers.ModelSerializer):
#     class MovieTitleSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Movie
#             fields = ('title',)

#     movies = MovieTitleSerializer(many=True, read_only=True)

#     class Meta:
#         model = Actor
#         fields = '__all__'

# class ActorListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actor
#         fields = '__all__'

# class ActorNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actor
#         fields = ('name',)


# class ReviewDetailSerializer(ReviewListSerializer):
#     movie_title = serializers.CharField(source='movie.title', read_only=True)

#     class Meta(ReviewListSerializer.Meta):
#         fields = ReviewListSerializer.Meta.fields + (
#             'movie_title',
#         )

#     def to_representation(self, instance):
#         rep = super().to_representation(instance)
#         rep['movie'] = rep.pop('movie_title', [])
#         return rep

# class ReviewContentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ('title', 'content',)

# class MovieDetailSerializer(serializers.ModelSerializer):

#     class ReviewContentSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Review
#             fields = ('title', 'content',)
    
#     class ActorNameSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Actor
#             fields = ('name',)

#     actors = ActorNameSerializer(many=True, read_only=True)
#     review_set = ReviewContentSerializer(many=True, read_only=True)

#     class Meta:
#         model = Movie
#         fields = '__all__'

