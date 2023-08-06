from django.db import models
from django.contrib import admin

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=245)
    subtitle = models.CharField( max_length=245)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    published_date = models.DateField(auto_now=False, auto_now_add=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    distributions_expense = models.FloatField()

    def __str__(self):
        return print(f"Title = {self.title}, Authors: {self.authors}, Category: {self.category}, Distributions Expense: {self.distributions_expense}")