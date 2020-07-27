from django.db import models

# Create your models here.
class Recipe(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)
    imageUrl = models.URLField()

