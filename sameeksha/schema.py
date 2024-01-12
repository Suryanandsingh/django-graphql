import graphene
import cinema.schema

class Query(cinema.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
