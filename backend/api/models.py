from django.db import models
from django.db.models import Model
from django.contrib import admin 


class Country(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    location = models.CharField(max_length=40)
    emoji = models.CharField(max_length=1)
    description = models.CharField(max_length=600)
    secondary_text = models.CharField(max_length = 900)


class Project(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    description = models.CharField(max_length=600)
    score = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


