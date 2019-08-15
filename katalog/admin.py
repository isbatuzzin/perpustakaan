from django.contrib import admin
from katalog.models import Author, Book, Genre, BookInstance, Language

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)