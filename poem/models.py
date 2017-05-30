from django.db import models
from stdimage import StdImageField
from django_jalali.db import models as jmodels
from django.utils import timezone

# Create your models here.
class Poem(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(null=True)
    image = StdImageField(upload_to='blogimage', blank=True, null=True,variations={'large':(850, 550,True),'thumbnail': (200, 200,True),})
    sound = models.FileField(upload_to='sounds', blank=True, null=True)
    def __str__(self):
        return self.title