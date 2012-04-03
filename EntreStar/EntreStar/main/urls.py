from django.conf.urls.defaults import *

urlpatterns = patterns('ComfortText.users.views',
    (r'^signup$', 'signup'),
    (r'^login$', 'userLogin'),
    (r'^logout$', 'userLogout'),
)

