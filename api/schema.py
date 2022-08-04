import graphene

from graphene_django import DjangoObjectType, DjangoListField
from .models import *



class BookType(DjangoObjectType):
    class Meta:
        model = Book 
        fields = '__all__'
        
class AuthType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'
        
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'
        
class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.Int())
    
    all_authors = graphene.List(AuthType)
    author = graphene.Field(AuthType, id=graphene.Int())
    
    all_categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, id=graphene.Int())
    
    
    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()
    
    def resolve_book(self, info, id):
        return Book.objects.get(pk=id)
    
    def resolve_all_authors(self, info, **kwargs):
        return Author.objects.all()
    
    def resolve_author(self, info, id):
        return Author.objects.get(pk=id)
    
    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()
    
    def resolve_category(self, info, id):
        return Category.objects.get(pk=id)
    
    
schema = graphene.Schema(query=Query)