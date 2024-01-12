from django.db import models

# Create your models here.


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    date_of_release = models.CharField(max_length=20, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    duration = models.IntegerField(blank=True, null=True) #that is in minutes
    genres = models.CharField(max_length=100)
    rating = models.FloatField(blank=True, null=True)
    votes = models.IntegerField(blank=True, null=True)
    gross_earning_in_mil = models.FloatField(blank=True, null=True, default=None)
    director = models.ForeignKey('Director', related_name='+', on_delete=models.CASCADE, null=True, blank=True)
    actor = models.ForeignKey('Actor', related_name='ActedBy+', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Director(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    date_of_birth = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=500, null=True)
    award_win = models.IntegerField(blank=True, null=True, default=None)
    no_of_movies = models.IntegerField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    date_of_birth = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=500, null=True)
    award_win = models.IntegerField(blank=True, null=True, default=None)
    no_of_movies = models.IntegerField(blank=True, null=True, default=None)


    def __str__(self):
        return self.name