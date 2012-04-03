from django.db import models

from EntreStar.users.models import StarUser 
from EntreStar.tags.models import TagOwner, Tag  
from django.core.files.storage import FileSystemStorage



# Create your models here.
"""
 File model
"""

fsi = FileSystemStorage(location='/site-media/images')
fsd = FileSystemStorage(location='/site-media/documents')


class Document(models.Model):
    file = models.FileField(upload_to='/site-media/documents',null=True, blank=True) 
    title=models.CharField(max_length=200, blank=True,null=True) 
    owner=models.ForeignKey(StarUser,related_name="documents",null=False,blank=False)
    #path=models.FilePathField(blank=False,null=False)  
    #type=models.CharField(max_length=200)

     
class Image(models.Model): 
    img=models.ImageField(upload_to='/site-media/images',null=True, blank=True)
    title=models.CharField(max_length=200, blank=True,null=True) 
    owner=models.ForeignKey(StarUser,related_name="images",null=False,blank=False)

    #path=models.FilePathField(blank=False,null=False)  
    #type=models.CharField(max_length=200)

    
   
    

