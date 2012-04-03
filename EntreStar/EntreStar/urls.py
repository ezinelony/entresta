from django.conf.urls.defaults import *
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import logging
logger = logging.getLogger(__name__)
 
 
urlpatterns = patterns('',
    # Examples:
   url(r'^$', 'EntreStar.main.views.home', name='home'), 
     
    (r'^site-media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.STATIC_URL}),
    url(r'', include('EntreStar.main.urls')), 
    url(r'users/', include('EntreStar.users.urls')), 
    url(r'profiles/', include('EntreStar.profiles.urls')),
    url(r'profile/', include('EntreStar.profiles.urls')),
    url(r'startups/', include('EntreStar.profiles.urls')),
    url(r'.*$', 'EntreStar.profiles.views.startup', name='login'),#slug
)
