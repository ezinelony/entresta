# Create your views here.
from django.template.context import RequestContext
from EntreStar.jobs.models import Job
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
import datetime
from EntreStar.tags.models import Tag
from EntreStar.utils import getReferrer
from django.http import HttpResponseRedirect
from EntreStar.profiles.models import CompanyProfile

def index(request):
    job = Job.objects.get(id=request.POST['id'])
    c = RequestContext(request,{'message':'','error':0,'data':job})
    return render_to_response('jobs/new.html', c) 

def openingsByCompany(request):
    profile=CompanyProfile.objects.get(id=request.POST['id'])
    jobs=profile.jobs
    c = RequestContext(request,{'message':'','error':0,'data':jobs})
    return render_to_response('openings.html', c) 

@login_required
def new(request):
    user=request.user
    ref =getReferrer(request,'new')
    request.session['ref'] = ref 
    if user.is_company() & request.POST:
        c = RequestContext(request,{'message':'','error':0})
        return render_to_response('jobs/new.html', c) 
    c = RequestContext(request,{'message':'You have no permission for the request','error':1})
    return  HttpResponseRedirect(ref)

@login_required
def create(request):
    user=request.user
    if user.is_company() & request.method=='POST':
        job= Job()
        job.active_duration=30 # days
        job.company=user.profile
        job.description=request.POST['description']
        job.title=request.POST['title']
        job.ownerType='CompanyProfile'
        job.salary_benefits=request.POST['salary_benefits']
        job.post_date=datetime.datetime.now()
        job.requirement=request.POST['requirement']
        job.type=request.POST['type']
        tag=Tag()
        tag.tags=request.POST['tag']+request.POST['description']+request.POST['requirement']
        job.tags=tag
        try:
            job.save()
            c = RequestContext(request,{'message':'Post successful','error':0,'data':job})
        except Exception ,e:
            c = RequestContext(request,{'message':e,'error':1,'data':job})
            return render_to_response('jobs/edit.html', c)  
        return render_to_response('jobs/index.html', c)  
    c = RequestContext(request,{'message':'You have no permission','error':1})
    return render_to_response('jobs/index.html', c)  
        
    