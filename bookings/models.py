from django.db import models
from divers.models import divers
# Create your models here.
class dive(models.Model):
    location= models.CharField(max_length=50,null=True)
    date = models.DateTimeField()
    diver = models.ForeignKey(divers,on_delete=models.CASCADE)
    cost = models.IntegerField(null=True)