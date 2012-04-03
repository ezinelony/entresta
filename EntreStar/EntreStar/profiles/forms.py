from django.forms import ModelForm
from EntreStar.profiles.models import CompanyProfile, StudentProfile
from django.forms.widgets import Textarea

class CompanyProfileForm(ModelForm):
    class Meta:
        model=CompanyProfile
        exclude = ('slug',)
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
    
    
class StudentProfileForm(ModelForm):
    class Meta:
        model=StudentProfile
        fields = ('resume','profile_pic','external_profile_pic',)