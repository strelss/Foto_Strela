from django.db import models
from gallery.models import *

class About_me(models.Model):
    my_foto = models.ImageField(upload_to='media/me')


    class Meta:
        verbose_name = 'Я на фотографии'
        verbose_name_plural = 'Я на фотографиях'


