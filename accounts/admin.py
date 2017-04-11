from django.contrib import admin
from .models import (UserProfile, IronMan,
                     Project, Folder,
                     Evaluate,  Product
                     )
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(IronMan)
admin.site.register(Project)
admin.site.register(Folder)


admin.site.register(Product)

class EvaluateAdmin(admin.ModelAdmin):
    list_display = ('team','project','performance','attitude')
    search_fields = ('team','project','client')

admin.site.register(Evaluate, EvaluateAdmin)