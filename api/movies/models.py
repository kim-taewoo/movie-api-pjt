from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    poster = models.URLField(max_length=200)
    rating = models.FloatField()
    pub_date = models.DateField()
    runtime = models.IntegerField()
    overview = models.TextField()
    audits = models.CharField(max_length=255)
    movie_cd = models.IntegerField()
    audi_cnt = models.IntegerField()

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=255)
    movie = models.ManyToManyField(Movie, blank=True, related_name='genres')

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)
    movie = models.ManyToManyField(Movie, blank=True, related_name='nations')

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=255)
    movie = models.ManyToManyField(Movie, blank=True, related_name='actors')

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=255)
    movie = models.ManyToManyField(Movie, blank=True, related_name='directors')

    def __str__(self):
        return self.name


class Review(models.Model):
    rating = models.IntegerField()
    content = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked_reviews')
    unlikes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='unliked_reviews')

    @property
    def likes_count(self):
        return self.likes.count()
    
    @property
    def unlikes_count(self):
        return self.unlikes.count()

    @property
    def formatted_time(self):
        return self.created_at