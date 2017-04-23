from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from tinymce.widgets import TinyMCE
# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    year = models.DateField(default='2011-11-11')
    date_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title  + " " + self.artist

class Song(models.Model):
    title = models.CharField(max_length=20)
    album = models.ForeignKey(Album)

    def __str__(self):
        return self.title+" " + str(self.album)

    def get_absolute_url(self):
        return self.title + " " + str(self.album)

from django.db import models
from tinymce.models import HTMLField

class MyModel(models.Model):
    ...
    content = HTMLField()