from django.forms import ModelForm
from EntreStar.profiles.models import CompanyProfile, StudentProfile
from django.forms.widgets import Textarea
from EntreStar.users.models import Student, Company

class StudentForm(ModelForm):
    class Meta:
        model=Student
 
class CompanyForm(ModelForm):
    class Meta:
        model=Company

    
