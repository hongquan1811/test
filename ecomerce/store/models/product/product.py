from django.db import models
from .category import Category
from .supplier import Supplier

class Product(models.Model):
    name = models.CharField(max_length=200)
    
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.CASCADE,
    )
    supplier = models.ForeignKey(
        Supplier,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name