from django.db import models

# Create your models here.
class Zipcode(models.Model):
    code = models.CharField(max_length=5)
    #poly = models.PolygonField()
    #objects = models.GeoManager()
    
class SAddress(models.Model):
    num = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.ForeignKey(Zipcode)
    #objects = models.GeoManager()
    
    
    

    
