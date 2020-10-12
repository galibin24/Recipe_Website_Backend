from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    recipes_owned = models.CharField(blank=True, max_length=120, default="")

