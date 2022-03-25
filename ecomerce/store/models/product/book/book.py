from django.db import models
from django.urls import reverse

from .author import Author
from .genre import Genre
from .publisher import Publisher
from ..product import Product

class Book(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    LANGUAGES = [
        ('en', 'English'),
        ('vi', 'Vietnamese'),
        ('kr', 'Korean'),
        ('cn', 'Chinese')
    ]
    language = models.CharField(
        max_length=3,
        choices=LANGUAGES,
    )
    number_of_pages = models.IntegerField()
    summary = models.TextField(max_length=500)
    isbn = models.CharField(max_length=20, unique=True)

    publisher = models.ForeignKey(
        Publisher, 
        null=True, 
        on_delete=models.CASCADE,
    )

    genres = models.ManyToManyField(Genre,)
    authors = models.ManyToManyField(Author,)


    def __str__(self):
        return self.product.name


