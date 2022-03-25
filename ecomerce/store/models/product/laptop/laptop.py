from django.db import models
from django.urls import reverse

from ..product import Product


class Laptop(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    ram = models.CharField(max_length=20)
    rom = models.CharField(max_length=20)
    cpu = models.CharField(max_length=20)
    screen = models.CharField(max_length=500)
    model = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.product.name
