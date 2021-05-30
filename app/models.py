from django.db import models

# Create your models here.
class feed(models.Model):
    name=models.CharField(max_length=100)
    rating=models.SmallIntegerField()
    fb=models.TextField()
class experience(models.Model):
    name=models.CharField(max_length=100)
    option=models.CharField(max_length=100)
    exp=models.TextField()