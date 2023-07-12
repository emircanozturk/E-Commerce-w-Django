from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Stuff(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.CharField(max_length=64, default="")
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to="stuff/")

    def __str__(self):
        return self.name