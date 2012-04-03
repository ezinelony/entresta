from django.db import models
#from EntreStar.utils.Polymorph import Polymorph
# Create your models here.
"""
Any model that extends TagOwner is tagable
"""
from EntreStar.utility.models import Polymorph 
from EntreStar.utility.meta import Meta_Polymorph




class TagOwner(Polymorph):
    ownerType=models.CharField(max_length=200, blank=False)
    
"""
  Tag
"""   
class Tag(models.Model):
    tags=models.CharField(max_length=200, blank=False)
    owner=models.OneToOneField(TagOwner,related_name="tags",null=False,blank=False)