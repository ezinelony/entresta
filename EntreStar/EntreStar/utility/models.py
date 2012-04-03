from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import simplejson
from django.utils.functional import Promise
from django.utils.encoding import force_unicode
from EntreStar.utility.meta import Meta_Polymorph

class Polymorph(models.Model):
    """
    An abstract base class that provides a ``real_type`` FK to ContentType.

    For use in trees of inherited models, to be able to downcast
    parent instances to their child types.

    """
    real_type = models.ForeignKey(ContentType, editable=False, null=True)


    # __metaclass__=Meta_Polymorph
  #  __metaclass__ = Meta_Polymorph
 
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.real_type = self._get_real_type()
        super(Polymorph, self).save(*args, **kwargs)

    def _get_real_type(self):
        return ContentType.objects.get_for_model(type(self))

    def cast(self):
        return self.real_type.get_object_for_this_type(pk=self.pk)

    class Meta:
        abstract = True


        
class ComplexEncoder(simplejson.JSONEncoder):
    def default(self, obj):
            if isinstance(obj, complex):
                return [obj.real, obj.imag]
            return simplejson.JSONEncoder.default(self, obj)
        
class LazyEncoder(simplejson.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_unicode(obj)
        return super(LazyEncoder, self).default(obj)
            
            