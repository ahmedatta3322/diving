from django.db import models
import os

# Create your models here.
class Divers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    user_name = models.CharField(max_length=50)
    photo = models.ImageField()
    cert = models.CharField(max_length=50,default="Dive master")
    n_dives = models.IntegerField(default=1)
    padi_code = models.IntegerField(default=0)


