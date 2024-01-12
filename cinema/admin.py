from django.contrib import admin

from cinema.models import Movie, Director, Actor

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)
