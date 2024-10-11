from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100)

class Car(models.Model):
    model_name = models.CharField(max_lengh=200)
    year = models.IntegerField(max)
    make_name = models.Fo
