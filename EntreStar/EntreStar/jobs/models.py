from django.db import models 
from EntreStar.addresses.models import SAddress
from EntreStar.tags.models import TagOwner, Tag
from EntreStar.profiles.models import CompanyProfile

#from EntreStar.addresses.models import Address

# Create your models here.

class Job(models.Model,TagOwner):
    title=models.CharField(max_length=200)
    description=models.TextField()
    requirement=models.TextField()
    post_date=models.DateField()
    updated_at=models.DateField(auto_now=True)
    company=models.ForeignKey(CompanyProfile,related_name='jobs')
    salary_benefits=models.CharField(max_length=200)
    tags=models.OneToOneField(Tag,null=True,blank=True)
    location=models.ForeignKey(SAddress)
    active_duration=models.IntegerField()
    type=models.CharField(max_length=200)
