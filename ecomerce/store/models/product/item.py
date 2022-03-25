from django.db import models
from .product import Product

class Item(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    price = models.FloatField()
    discount = models.CharField(max_length=4)
    image = models.ImageField(upload_to = 'uploads/images/')