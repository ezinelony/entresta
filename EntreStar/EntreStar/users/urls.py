from django.conf.urls.defaults import *

urlpatterns = patterns('EntreStar.users.views',
    (r'^signup$', 'signup'),
    (r'^login$', 'ulogin'),
    (r'^logout$', 'userLogout'),
    (r'^student_join', 'sjoin'),
    (r'^startup_join', 'pjoin'),
 
)

