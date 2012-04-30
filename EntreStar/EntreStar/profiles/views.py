# Create your views here.
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from EntreStar.profiles.models import Profile, CompanyProfile, StudentProfile
from EntreStar.utils import getReferrer
from EntreStar.tags.models import Tag 
from EntreStar.networks.models import Network
from django.forms.models import modelformset_factory, inlineformset_factory
from EntreStar.documents.models import Image, Document
from EntreStar.users.models import Student, Company
from EntreStar.profiles.forms import StudentProfileForm
from EntreStar.settings import PROJECT_PATH, LOGO_URL
from django.http import HttpResponseRedirect, HttpResponse
import json

@login_required(login_url="/")
def new(request):
    c = RequestContext(request,{'message':"",'error':0})
    file= 'newStudentProfile.html'
    if request.user.is_company():
        file='newCompanyProfile.html'
    return render_to_response(file, c)
 
@login_required(login_url="/")
def profile(request):
    #if usr is not student redirect to startup
    print "----"
    if not request.method=='POST':
        return newStudentProflie(request)
    return createNewStudentProflie(request)
    
def newStudentProflie(request):
    user=request.user 
    try :
        userProfile= user.profile
    except Exception, e:
        print str(e)
        StudentFormSet =modelformset_factory(StudentProfile,form=StudentProfileForm) 
        StudentFormSet = StudentFormSet(queryset=StudentProfile.objects.filter(owner=user))#instance=userProfile)

        c = RequestContext(request,{"formset": StudentFormSet,'new_profile':True})
        return render_to_response("profiles/index.html", c)
    new_profile=False
    p=userProfile.cast() 
    d={'new_profile':new_profile,"error":0, "message":""}
    if  bool(p.profile_pic):
        d['profile_pic_url'] =p.profile_pic.url
        d['pic_exists'] =True
    if bool(p.resume):
        d['resume_url']=p.resume.url
        d['resume_exists'] =True
    c = RequestContext(request,d)
            
    return render_to_response("profiles/index.html", c)

def createNewStudentProflie(request):
    user=request.user
    try :
        new_profile=False
        userProfile= user.profile
    except :
        new_profile=True
        userProfile= StudentProfile()
        userProfile.owner=user
        userProfile.ownerType="StudentProfile"           
        form = StudentProfileForm(request.POST, request.FILES)
        try:
            profile=form.save(commit=False)
            
            profile.owner=user
            profile.ownerType="StudentProfile"  
            # profile.save()
            for k,v in request.FILES.items() :
                if 'resume' in k:
                    profile.resume=v
                if 'profile_pic' in k:
                    profile.profile_pic=v
            profile.save()     
           
        except Exception, e:
            print str(e)
            new_profile=True
    userProfile= user.profile
    p=userProfile.cast()
    print  p.resume ==None
    d={'new_profile':new_profile,"error":0, "message":""}
    if  bool(p.profile_pic):
        d['profile_pic_url'] =p.profile_pic.url
        d['pic_exists'] =True
    if bool(p.resume):
        d['resume_url']=p.resume.url
        d['resume_exists'] =True
    c = RequestContext(request,d)
            
    return render_to_response("profiles/index.html", c)

def startup(request,id):
    print str(id)+""
    
    ref=getReferrer(request,'startup')
    request.session['ref'] = ref 
    try:
        editable=False
        user=request.user
        company= CompanyProfile.objects.get(pk=id)
        if user.is_authenticated:
            if user.id==company.owner.id:
                editable=True
    except Exception,e:
        print str(e)
        return   HttpResponseRedirect(ref)
    d={'editable':editable,"error":0, "message":"","profile":company} 
    c = RequestContext(request,d)  
    return render_to_response("profiles/startup.html", c) 
   
        
"""
edit profile: requires logged in user 
"""
#@login_required(login_url="/")
def edit(request):
    #c = RequestContext(request,{'message':"",'error':0})
    try :
        user= request.user
        profile= user.cast().profile.cast()
        print profile
        setattr(profile,request.GET['attribute'],request.GET['value'])
        profile.save()
        json_obj = json.dumps({'message':" Update successful",'error':0})
    except Exception ,e :
        print str(e)
        json_obj = json.dumps({'message':"Unsuccessful update!!!",'error':1})
    return  HttpResponse(json_obj, mimetype='application/json') 

@login_required(login_url="/")
def update(request): 
    
    c = RequestContext(request,{'message':"",'error':0})
    try :
        profile = Profile.objects.get(id=request.POST['profileId'])
        if profile.owner != request.user: # Not the owner of the profile
            return    
    except Exception ,e :
        c = RequestContext(request,{'message':e,'error':1})
    return render_to_response('edit.html', c) 

def details(request):
    c = RequestContext(request,{'message':"",'error':0})
    ref =getReferrer(request,'details')
    request.session['ref'] = ref
    file= "studentProfile.html"
    try :
        profile = Profile.objects.get(id=request.POST['profileId'])      
        if profile.is_company() :
            file="companyProfile.html"
        return render_to_response(file, c)     
    
    except Exception ,e :
        msg=e
        error =1
    c = RequestContext(request,{'message':msg,'error':error})
    return render_to_response(file, c) 
