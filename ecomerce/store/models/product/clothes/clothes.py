from django.db import models
from django.urls import reverse

from ..product import Product

class Clothes(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    material = models.CharField(max_length=50)


    def __str__(self):
        return self.product.name


