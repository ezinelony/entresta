from django.conf.urls.defaults import *

urlpatterns = patterns('EntreStar.profiles.views',
    (r'^edit$', 'edit'), 
    (r'^/u', 'profile'), 
    (r'(?P<id>.*)$', 'startup'), 

    

    
 
)

