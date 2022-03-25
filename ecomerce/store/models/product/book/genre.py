from django.db import models
class Genre(models.Model):
    name = models.CharField(max_length=200)
    age_range = models.CharField(max_length=20)
    description = models.TextField(max_length=20)

    def __str__(self):
        return self.name