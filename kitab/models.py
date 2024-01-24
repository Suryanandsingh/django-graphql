from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)
    genres = models.CharField(max_length=100)
    rating = models.FloatField(blank=True, null=True)
    no_of_pages = models.IntegerField(default=0)
    author = models.ForeignKey('Author', related_name='author', on_delete=models.CASCADE)
    rank = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(default=0)
    quantity = models.IntegerField(blank=True, null=True)
    isbn = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    dimensions = models.CharField(max_length=200, blank=True, null=True)
    country_of_origin = models.CharField(max_length=200)
    publication_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.CharField(max_length=100, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    award_win = models.IntegerField(blank=True, null=True, default=None)
    notes = models.TextField(default="")
    no_of_books = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name