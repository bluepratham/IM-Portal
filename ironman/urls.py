from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ironmanHome),
    # url(r'^add_scrum/', views.Scrum_Create),
    url(r'^contact/', views.contact),
    url(r'^(\d{1,2})/request/$', views.req_session),
    url(r'^synthesis/', views.synth), #TODO: make url for synthesis keeping in mind anonymous users should also have access
    url(r'^(\d{1,2})/$', views.project ),
    url(r'^(\d{1,2})/bug/$', views.req_bug),
    url(r'^(\d{1,2})/(.*)/$', views.share),
    url(r'^(?P<name>scrum)/$', views.scrumlist.as_view())
]