from enum import auto
from tkinter.tix import AUTO
from django.db import models

# Create your models here.

class Movies(models.Model):
    MovieName=models.CharField(max_length=255)
    ReleasedYear=models.IntegerField(max_length=4)
    Rating=models.FloatField(max_length=4)
    Languages=models.TextField()
    
    
    class Meta:
        db_table="Movies"
        
    def __str__(self):
        return self.name+" has choosed"