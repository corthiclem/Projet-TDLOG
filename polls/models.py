import datetime 

from django.db import models
from django.utils import timezone

#Modele qui represente les matieres
class Discipline(models.Model):
    label = models.CharField(max_length = 1000)
    def __str__(self):
        return self.label
        
#Modele qui represente les ecoles
class School(models.Model):
    name = models.CharField(max_length = 1000)
    capacity = models.IntegerField(default=0)
    descrip = models.TextField(max_length = 1000)
    auto_id = models.AutoField(primary_key = True)
    def __str__(self):
        return self.name


