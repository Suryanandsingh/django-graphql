import graphene
import cinema.schema
import kitab.schema

class Query(cinema.schema.Query, kitab.schema.Query, graphene.ObjectType):
    pass

class Mutation(kitab.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
