from django.db import models
 
from EntreStar.users.models import StarUser 
from EntreStar.networks.models import Network
from EntreStar.tags.models import Tag, TagOwner 
from EntreStar.addresses.models import SAddress 
from EntreStar.autoslug.fields import AutoSlugField
from EntreStar.settings import RESUME_URL, LOGO_URL
#from EntreStar.networks.models import Network

#from EntreStar.documents.models import Document

# Create your models here.
class Profile(TagOwner):
    owner=models.OneToOneField(StarUser,related_name="profile",null=False,blank=False)
    searchable=models.BooleanField()

    tags= models.OneToOneField(Tag,null=True,blank=True)
    
    @models.permalink
    def get_view_url(self):
        return ('profiles.views.details', [str(self.id)])
    
    @models.permalink
    def get_edit_url(self):
        return ('profiles.views.edit', [str(self.id)])
    
    def is_company(self):
        return self.ownerType=='CompanyProfile'

    
  
    
class CompanyProfile(Profile):
    name = models.CharField(max_length=200,null=False)
    description = models.CharField(max_length=200,null=True, blank=True)
    address = models.ForeignKey(SAddress,null=True, blank=True) 
    employees = models.IntegerField(null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True,max_length=255)
    logo =models.ImageField(upload_to=LOGO_URL,null=True, blank=True)
    external_logo=models.URLField(null=True, blank=True)
    #fbook= models.CharField(max_length=200,null=False)
    
class StudentProfile(Profile):
    resume =  models.FileField(upload_to=RESUME_URL,null=True, blank=True) 
    network = models.ForeignKey(Network,null=True, blank=True)
    profile_pic =models.ImageField(upload_to=LOGO_URL,null=True, blank=True)
    external_profile_pic=models.URLField(null=True, blank=True)
    


    