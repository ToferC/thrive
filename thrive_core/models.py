from django.db import models
from django.utils import timezone

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
