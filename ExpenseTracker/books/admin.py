from django.contrib import admin
from django.apps import apps
from .models import Book, Author, Publisher, Category

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category, )
admin.site.register(Publisher)