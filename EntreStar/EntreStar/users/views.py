# Create your views here.
# Create your views here.
from django.template.context import RequestContext
from EntreStar.users.models import Company, Student
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from EntreStar.utils import getReferrer
from django.utils import simplejson as json
from EntreStar.utility.models import LazyEncoder, LazyEncoder
from EntreStar.profiles.models import CompanyProfile
from django.db.backends.dummy.base import IntegrityError
 

def signup(request):
    msg=''
    c = RequestContext(request,{'message':msg}) 
    ref =getReferrer(request,'signup')
    request.session['ref'] = ref   
    if request.method == 'POST':

        if not 'email' in request.POST or not 'password' in request.POST:
            msg="Email and password are required"
            response={'message':msg,'error':1}
            c = RequestContext(request,response) 
            return render_to_response('users/signup.html', c)   
        eLength=len(request.POST['email'])
        pLength=len(request.POST['password'])
        if eLength==0 or pLength==0:
            msg="Email and password are required"
            response={'message':msg,'error':1}
            if 'async' in request.POST :
                print "In POST 1"
                if  request.POST['async']=='1' :
                    json_obj =  json.dumps(response,cls=LazyEncoder)
                    return HttpResponse(json_obj, mimetype='application/json')
            c = RequestContext(request,{'message':msg}) 
            return render_to_response('users/signup.html', c)      
        return createUser(request)
    elif request.user.is_authenticated() :
        if 'async' in request.POST :
            if  request.POST['async']=='1' :
                json_obj =  json.dumps(response,cls=LazyEncoder)
                return HttpResponse(json_obj, mimetype='application/json')
        return   HttpResponseRedirect(ref)
    
        if 'async' in request.POST :
            if  request.POST['async']=='1' :
                json_obj =  json.dumps(response,cls=LazyEncoder)
                return HttpResponse(json_obj, mimetype='application/json')
    return render_to_response('users/signup.html', c)

def createUser(request): 
    msg='' 
    error=0             
    try:
        
        if request.POST['type'] =='Student' :
            userdao = Student.objects.create_user(username=request.POST['email'],email=request.POST['email'], password=request.POST['password'])  
        else :
            userdao = Company.objects.create_user(username=request.POST['email'],email=request.POST['email'], password=request.POST['password'])  
        print "ERROR"
        userdao.save()
    
        user =authenticate(username=request.POST['email'], password=request.POST['password'])
        login(request,user)  
        if user.is_authenticated():
            profile_link="/profile"
            if request.POST['type'] =='Company' :
                
                profile= CompanyProfile()
                profile.owner=userdao
                profile.ownerType="CompanyProfile"
                profile.name=request.POST['name']
                profile.save()
                profile_link="/"+profile.slug

        if 'async' in request.POST :
            if  request.POST['async']=='1' :
                response={"message":"Successful","link":profile_link,"error":0}
                
                json_obj =  json.dumps(response,cls=LazyEncoder)
                return HttpResponse(json_obj, mimetype='application/json')
        
        return   HttpResponseRedirect(request.session['ref'])
        '''  
            Error when email already exists
         '''
    except Exception ,e :
        if "Duplicate" in str(e):
            msg="Email address already exists, please enter a different one "
        else:
             msg="Try again"
        print str(e)
        error=1
    if 'async' in request.POST :
        if  request.POST['async']=='1' :
            response={"message":msg,"error":error}
            json_obj =  json.dumps(response,cls=LazyEncoder)
            return HttpResponse(json_obj, mimetype='application/json')  
    c = RequestContext(request,{'message':msg,'error':error})    
    return render_to_response('users/signup.html', c)
    

def userLogin(request):
    msg=''
    ref =getReferrer(request,'login')        
    c = RequestContext(request,{'message':msg})
    if  request.user.is_authenticated() :
        msg ='Logged In'
        c = RequestContext(request,{'message':msg})
        return render_to_response('index.html', c)
    elif request.method == 'POST' :
        if logUserIn(request) ==1:
            c = RequestContext(request,{'message':"Login Successful",'error':0})
            return render_to_response('index.html', c)  
        else :
            c = RequestContext(request,{'message':"Login unsuccessful",'error':1})
            return render_to_response('users/login.html', c)  
    else:
        c = RequestContext(request,{'message':msg})
        return render_to_response('users/login.html', c)  

def ulogin(request):
    successful=logUserIn(request)
    ref =getReferrer(request,'ulogin') 
    error=1
    msg=""
    link=""
    if not request.method == 'POST' :
        return render_to_response('users/login.html') 
    if successful==1:
        error=0
        link=ref
    else :
        error=1
        msg=" Username and password did not match!"
    response={"message":msg,"error":error,"link":link}
    json_obj =  json.dumps(response,cls=LazyEncoder)
    return HttpResponse(json_obj, mimetype='application/json')  
        
                
def logUserIn(request):
    try:
        user =authenticate(username=request.POST['email'], password=request.POST['password'])
        login(request,user) 
    except Exception, e :
        print e
        return 0 
    return 1
      
def sjoin(request):
    userLogout(request)
    ref =getReferrer(request,'sjoin') 
    request.session['ref'] = ref 
    if request.user.is_authenticated():
        c = RequestContext(request)
        return render_to_response('index.html', c)
    c = RequestContext(request) 
    return render_to_response('users/student_join.html', c)  

def pjoin(request):
    ref =getReferrer(request,'pjoin') 
    request.session['ref'] = ref 
    if request.user.is_authenticated():
        c = RequestContext(request)
        return render_to_response('index.html', c)
    c = RequestContext(request) 
    return render_to_response('users/startup_join.html', c)  
 
def userLogout(request):
    logout(request)
    if 'ref' in request.session:
        del request.session['ref']
    ref =getReferrer(request,'logout')    
    return  HttpResponseRedirect(ref)
    
