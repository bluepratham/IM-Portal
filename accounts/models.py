from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
# Create your models here.


class IronMan(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    mid_name = models.CharField(max_length=30, blank=True , default='')
    last_name = models.CharField(max_length=20)
    time = models.DateTimeField(default=datetime.now)
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
        return self.product_name 


class Folder(models.Model):
    project = models.ForeignKey(Project)
    team = models.ForeignKey(User, limit_choices_to={'groups__name': 'ironmen'}, related_name='proj_team' )
    client = models.ForeignKey(User, limit_choices_to={'groups__name': 'Client'}, related_name='proj_client')
    mentor = models.CharField(default='', max_length=40)
    prob_stat = models.TextField()
    vertical = models.CharField(max_length=20)
    time = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.team) + " " + str(self.project)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.team) +" "+ str(self.project))
        super(Folder, self).save(*args, **kwargs)



class Evaluate(models.Model):
    team = models.ForeignKey(User, limit_choices_to=
            {'groups__name': 'ironmen'}, related_name='eval_team')
    client = models.ForeignKey(User, limit_choices_to={
                'groups__name': 'Client'}, related_name='eval_client')
    project = models.ForeignKey(Project)
    performance = models.IntegerField(default=0)
    attitude = models.IntegerField(default=0)
    feedback = models.TextField(default='')
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        a = self.performance + self.attitude
        return str(self.team) + " " + str(self.project) + " " + str(a)

class Product(models.Model):
    prod_name = models.CharField(max_length=15)

    def __str__(self):
        return self.prod_name

