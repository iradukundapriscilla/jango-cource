from django.db import models

# Create your models here.

class Detail(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    age = models.IntegerField()
    phonumber = models.IntegerField()
