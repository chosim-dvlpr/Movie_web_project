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
    adult = models.BooleanField()
    backdrop_path = models.TextField()
    # genre_ids = models.ForeignKey(Genre, on_delete=CASCADE, related_name='movie_set')
    # "id"= 713704
    original_language = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.TextField()
    release_date = models.DateTimeField()
    title = models.CharField(max_length=100)
    video = models.BooleanField
    vote_average = models.FloatField()
    vote_count = models.IntegerField()


# class Review(models.Model):
#     title = models.CharField(max_length=100)
#     movie_title = models.CharField(max_length=50)
#     rank = models.IntegerField()
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

# class Comment(models.Model):
#     content = models.TextField()
#     review = models.ForeignKey(Review, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

