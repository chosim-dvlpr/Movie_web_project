from django.db import models
from django.conf import settings

# class Actor(models.Model):
#     name = models.CharField(max_length=100)

# class Movie(models.Model):
#     title = models.CharField(max_length=100)
#     overview = models.TextField()
#     release_date = models.DateTimeField()
#     poster_path = models.TextField()
    # actors = models.ManyToManyField(Actor, related_name='movies')

# genre 모델 추가해야함 for genre_ids

class Movie(models.Model):
    adult = models.CharField(max_length=20, null=True)
    backdrop_path = models.TextField(null=True)
    # genre_ids = models.ForeignKey(Genre, on_delete=CASCADE, related_name='movie_set')
    # "id"= 713704
    original_language = models.CharField(max_length=100, null=True)
    original_title = models.CharField(max_length=100, null=True)
    overview = models.TextField(null=True)
    popularity = models.FloatField(null=True)
    poster_path = models.TextField(null=True)
    release_date = models.CharField(null=True, max_length=50)
    title = models.CharField(max_length=100, null=True)
    video = models.CharField(null=True, max_length=20)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)


class Review(models.Model):
    title = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # movie_title = models.CharField(max_length=50)
    # rank = models.IntegerField()
    content = models.TextField(null=True)
    rating = models.IntegerField(null=True)
    recommendation = models.TextField(null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

# class Comment(models.Model):
#     content = models.TextField()
#     review = models.ForeignKey(Review, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

