from django.conf import settings
from django.db import models

class Task (models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField
    done = models.BooleanField


# Create your models here.
