import graphene
from graphene_django import DjangoObjectType


from kitab.models import Book, Author

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        # fields = '__all__'



class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        # fields = '__all__'


class KitabQuery(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)

    def resolve_all_books(self, info):
        return Book.objects.filter(is_active=True)
    

    def resolve_all_authors(self, info):
        return Author.objects.filter(is_active=True)

class BookCreateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        genres = graphene.String(required=True)
        description = graphene.String(required=True)
        no_of_pages = graphene.Int(required=True)
        author = graphene.String(required=True)
        quantity = graphene.Int(required=True)
        isbn = graphene.String(required=True)
        publisher = graphene.String(required=True)
        language = graphene.String(required=True)
        country_of_origin = graphene.String(required=True)
        publication_date = graphene.String(required=True)
        image = graphene.String()
        rating = graphene.Float()
        rank = graphene.Int()
        weight = graphene.Int()
        dimensions = graphene.String()

    book = graphene.Field(BookType)

    def mutate(self, info, **kwargs):
        book = Book.objects.create(**kwargs)
        return BookCreateMutation(book=book)
    
class BookUpdateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        id = graphene.ID(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, id, title, **kwargs):
        try:
            book = Book.objects.get(id=id)
            book.title = title
            book.save()
        except:
            book = None
        return BookUpdateMutation(book=book)
    
class BookDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, id):
        try:
            book = Book.objects.get(id=id)
            book.delete()
        except:
            book = None
        return BookDeleteMutation(book=book)


class AuthorCreateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        image = graphene.String()
        date_of_birth = graphene.String()
        nationality = graphene.String()
        award_win = graphene.Int()
        no_of_books = graphene.Int()
        notes = graphene.String()
    
    author = graphene.Field(AuthorType)

    def mutate(self, info, **kwargs):
        author = Author.objects.create(**kwargs)
        return AuthorCreateMutation(author=author)

class AuthorUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()

    author = graphene.Field(AuthorType)

    def mutate(self, info, id, name):
        try:
            author = Author.objects.get(pk=id)
            author.name = name
            author.save()
        except:
            author = None
        return AuthorUpdateMutation(author=author)

class AuthorDeleteMuatation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    author = graphene.Field(AuthorType)

    def mutate(self, info, id):
        try:
            author = Author.objects.get(pk=id)
            author.delete()
        except:
            author = None
        return AuthorDeleteMuatation(author=author)


class Query(KitabQuery):
    pass

class Mutation:
    #Book
    create_book = BookCreateMutation.Field()
    update_book = BookUpdateMutation.Field()
    delete_book = BookDeleteMutation.Field()

    #Author
    create_author = AuthorCreateMutation.Field()
    update_author = AuthorUpdateMutation.Field()
    delete_author = AuthorDeleteMuatation.Field()
