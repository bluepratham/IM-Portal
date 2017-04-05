from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Scrum(models.Model):
    comp_yest = models.CharField(max_length=500)
    roadblk = models.CharField(max_length=500,blank=True)
    plan_tdy = models.CharField(max_length=500)
    learning = models.CharField(max_length=500,blank=True)
    date = models.DateField(default='2011-11-11')
    created_by = models.CharField(max_length=50)

    def __str__(self):
        return self.created_by + " " + str(self.date)