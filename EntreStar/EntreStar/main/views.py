# Create your views here.
from django.template.context import RequestContext
from django.shortcuts import render_to_response 

def home(request): 
    popup_login=False
    next=""
    if 'next' in request.GET and not request.user.is_authenticated():
        popup_login=True
        next=request.GET['next']
    d={'message':"",'error':0,"popup_login":popup_login,"next":next}
    c = RequestContext(request,d)
    return render_to_response('index.html', c) 