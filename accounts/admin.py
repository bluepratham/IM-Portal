from django.contrib import admin
from .models import UserProfile, IronMan, Project, Folder
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(IronMan)
admin.site.register(Project)
admin.site.register(Folder)