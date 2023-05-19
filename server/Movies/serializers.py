from rest_framework import serializers
from .models import Movie, Review

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields= '__all__'

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

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'title', 'content',)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

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

