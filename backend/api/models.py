from django.db import models
from django.db.models import Model
import uuid

class Country(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    


class Project(models.Model):
