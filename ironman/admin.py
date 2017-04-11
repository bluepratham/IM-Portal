from django.contrib import admin
from .models import Scrum, SessionReq, synthesis, Bug, ShareDoc
# Register your models here.

admin.site.register(Scrum)
admin.site.register(SessionReq)
admin.site.register(synthesis)
admin.site.register(Bug)
admin.site.register(ShareDoc)
