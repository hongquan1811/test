from django.db import models
from .clothes import Clothes


class Pjamas(models.Model):
    type = models.CharField(max_length=20)

    clothes = models.OneToOneField(
        Clothes,
        on_delete=models.CASCADE,
        primary_key=True,
    )