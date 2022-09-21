from django.db import models

# Create your models here.
class MyWatchlistItem(models.Model):
    watched_movie = models.CharField(max_length=255)
    movie_title = models.CharField(max_length=255)
    movie_rate = models.IntegerField()
    release_date = models.DateField()
    movie_review = models.CharField(max_length=255)

