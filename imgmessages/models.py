from __future__ import unicode_literals
from django.db import models

class ImgMessage(models.Model):
    img = models.ImageField(upload_to='img')
    text = models.CharField(max_length=200)
    def __str__(self):
       return str(self.id)+", "+str(self.img)