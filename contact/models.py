from django.db import models

#agregamos la libreria para manejar fechas
from datetime import date

from portfolio.models import Project

# Create your models here.

class Participant(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    content= models.TextField()
    pub_date= models.DateField()
    mod_date= models.DateField(default=date.today)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant)

    def __str__(self):
        return self.name
