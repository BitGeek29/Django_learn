#from django.db import models

# Create your models here.
from djongo import models
import json


class Report(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Entry(models.Model):
    report = models.ArrayField(
        model_container=Report
    )    
    headline = models.CharField(max_length=255)    

e = Entry()
e.report = json.load(open('/workspace/Django_learn/Datasets/covid19.json'))
e.headline = 'Djongo is the best Django and MongoDB connector'
e.save()