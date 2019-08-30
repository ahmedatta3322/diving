from django.db import models

# Create your models here.
class divers(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    nationalty = models.CharField(max_length=50)
    cert = models.CharField(max_length=50)
    numberofdives = models.IntegerField()
    location = models.CharField(max_length=50)
    availibilty = models.CharField(max_length=50)
    image = models.ImageField(null=True,upload_to='divers/')
    gcost = models.PositiveSmallIntegerField(null=True)
    icost = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return self.name 
    