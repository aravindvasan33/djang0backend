from django.db import models

# Create your models here.
class Hotels(models.Model):
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)


def __str__(self):
    return self.city