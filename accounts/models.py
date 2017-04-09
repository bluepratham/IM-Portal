from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=20, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    mock_client = models.ForeignKey(User,related_name='client',null=True,blank=True ,default='',
                                    limit_choices_to={'groups__name': 'Client'})

    def __str__(self):
        return self.user.username + self.city



def create_profile(sender, **kwargs):
    print(kwargs['created'],kwargs['instance'])
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user = kwargs['instance'])

post_save.connect(create_profile, sender=User)