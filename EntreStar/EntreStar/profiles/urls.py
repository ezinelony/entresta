from django.conf.urls.defaults import *

urlpatterns = patterns('EntreStar.profiles.views',
    (r'^$', 'profile'), 
    (r'^edit$', 'edit'), 
    (r'^(?P<id>.*)$', 'startup'), 
    
 
)

