from django.db import models
from django.contrib.auth.models import UserManager

from django.contrib.auth.models import User
from EntreStar.utility.models import Polymorph
"""
 Star User class
"""
# Create your models here.    
class StarUser(User, Polymorph):
    objects=UserManager() 
    #type = models.CharField(max_length=100, blank=False)
    
    def is_company(self):
        return True
    
class Student(StarUser):
    objects=UserManager() 

    
        
class Company(StarUser):
    objects=UserManager() 

        
    