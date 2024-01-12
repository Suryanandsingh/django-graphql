import graphene
from graphene_django import DjangoObjectType
from django.core.exceptions import ObjectDoesNotExist

from cinema.models import Movie, Director, Actor

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = '__all__'

class DirectorType(DjangoObjectType):
    class Meta:
        model = Director
        fields = '__all__'

class ActorType(DjangoObjectType):
    class Meta:
        model = Actor
        fields = '__all__'


class CinemaQuerys(graphene.ObjectType):
    #Movies query
    all_movies = graphene.List(MovieType)
    get_movie = graphene.Field(MovieType, movie_id=graphene.Int(required=True))

    # Directors Query
    all_directors = graphene.List(DirectorType)
    get_director = graphene.Field(DirectorType, name=graphene.String(required=True))

    # Actor Query
    all_actors = graphene.List(ActorType)
    get_actor = graphene.Field(ActorType, name=graphene.String(required=True))


    ## Movie details
    def resolve_all_movies(self, info):
        return Movie.objects.all()
    
    def resolve_get_movie(self, info, movie_id):
        try:
            return Movie.objects.get(movie_id=movie_id)
        except ObjectDoesNotExist:
            return "This movie is not available." 


    ## Director details
    def resolve_all_directors(self, info):
        return Director.objects.all()
    
    def resolve_get_director(self, info, name):
        try:
            return Director.objects.get(name=name)
        except ObjectDoesNotExist:
            return "This director is not exists." 



    ## Actore details
    def resolve_all_actors(self, info):
        return Actor.objects.all()
    
    def resolve_get_actor(self, info, name):
        try:
            return Actor.objects.get(name=name)
        except ObjectDoesNotExist:
            return "This actor is not exists." 
    
class Query(CinemaQuerys):
    pass