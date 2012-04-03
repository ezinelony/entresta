from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model


class Authentication(ModelBackend):
    
    def authenticate(self, username=None, password=None):
        try:
            user = self.user_class.objects.get(username=username)
            print user
            if user.check_password(password):
                return user
        except self.user_class.DoesNotExist:
            
            return None
        
    def get_user(self, user_id):
        try:
            return self.user_class.objects.get(pk=user_id)
        except self.user_class.DoesNotExist:
            return None

    @property
    def user_class(self):
        if not hasattr(self, '_user_class'):
            self._user_class = get_model(*settings.CUSTOM_USER_MODEL.split('.', 2))
            if not self._user_class:
                raise ImproperlyConfigured('Could not get custom user model')
        return self._user_class
    
class StarUserModelBackend(Authentication):
    
    def __unicode__(self):
        return '%s %s',self.username," StarUserModelBackend"

    

class SocialMediaModelBackend(Authentication):
    
    def authenticate(self, user=None):
        try:
            u=user
            user = self.user_class.objects.get(username=user.username)
            if user.password==u.password:
                return user
        except self.user_class.DoesNotExist:
            return None
    
    def __unicode__(self):
        return '%s %s',self.username," StarUserModelBackend"
    
    