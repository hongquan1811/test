from django.db import models
from .clothes import Clothes


class Pjamas(models.Model):
    SEASONS = [
        ('sp', 'Srping'),
        ('su', 'Summer'),
        ('fa', 'Fall'),
        ('wi', 'Winter')
    ]
    season = models.CharField(
        max_length=3,
        choices=SEASONS,
    )

    clothes = models.OneToOneField(
        Clothes,
        on_delete=models.CASCADE,
        primary_key=True,
    )