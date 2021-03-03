from django.db import models

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=150)




class Color(models.Model):
    area = models.ForeignKey(Area, on_delete=models.PROTECT, related_name='colors')
    FILL_TYPE = [
        ('color', 'Color'),
        ('gradient', "Gradiend")
    ]
    fill_type = models.CharField(choices=FILL_TYPE, max_length=50)
    color = models.CharField(max_length=100)
    angle = models.FloatField()

class Point(models.Model):
    area = models.ForeignKey(Area, on_delete=models.PROTECT, related_name='points')
    lat = models.FloatField()
    long = models.FloatField()
