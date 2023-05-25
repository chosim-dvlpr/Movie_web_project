# Generated by Django 3.2 on 2023-05-25 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.CharField(max_length=20, null=True)),
                ('backdrop_path', models.TextField(null=True)),
                ('original_language', models.CharField(max_length=100, null=True)),
                ('original_title', models.CharField(max_length=100, null=True)),
                ('overview', models.TextField(null=True)),
                ('popularity', models.FloatField(null=True)),
                ('poster_path', models.TextField(null=True)),
                ('release_date', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('video', models.CharField(max_length=20, null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('vote_count', models.IntegerField(null=True)),
                ('like_users', models.ManyToManyField(related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Similarmovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.CharField(max_length=20, null=True)),
                ('backdrop_path', models.TextField(null=True)),
                ('original_language', models.CharField(max_length=100, null=True)),
                ('original_title', models.CharField(max_length=100, null=True)),
                ('overview', models.TextField(null=True)),
                ('popularity', models.FloatField(null=True)),
                ('poster_path', models.TextField(null=True)),
                ('release_date', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('video', models.CharField(max_length=20, null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('vote_count', models.IntegerField(null=True)),
                ('movie', models.ManyToManyField(related_name='similar_movie', to='Movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(null=True)),
                ('rating', models.IntegerField(null=True)),
                ('recommendation', models.TextField(null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movies.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
