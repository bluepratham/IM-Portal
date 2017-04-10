from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class IronMan(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    mid_name = models.CharField(max_length=30, blank=True , default='')
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.username +" " + self.first_name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=20, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    team_members = models.ManyToManyField(IronMan,blank=True ,default='')

    def __str__(self):
        return self.user.username + self.city



def create_profile(sender, **kwargs):
    print(kwargs['created'],kwargs['instance'])
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user = kwargs['instance'])

post_save.connect(create_profile, sender=User)


class Project(models.Model):
    product_name = models.CharField(max_length=30)
    timeInWeeks  = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name + " " + str(self.timeInWeeks) + "week/s"


class Folder(models.Model):
    project = models.ForeignKey(Project)
    team = models.ForeignKey(User, limit_choices_to={'groups__name': 'ironmen'}, related_name='proj_team' )
    client = models.ForeignKey(User, limit_choices_to={'groups__name': 'Client'}, related_name='proj_client')

    def __str__(self):
        return str(self.team) + " " + str(self.project)