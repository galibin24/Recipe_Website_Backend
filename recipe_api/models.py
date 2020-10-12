from django.db import models
from django.conf import settings

# Create your models here.
class Recipe(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=1000)
    imageUrl = models.URLField()
    recipe_type = models.CharField(
        max_length=2,
        choices=[('LH','Lunch'), ('DI','Dinner'), ('DE','Dessert')],
        default='DI')
    preperation_minutes = models.IntegerField(blank=False, null=False, default=60)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipes",
    )

