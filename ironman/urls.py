from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ironmanHome),
    url(r'^add_scrum/', views.Scrum_Create),
    url(r'^contact/', views.contact),
    url(r'^request/', views.req_session),
    url(r'^synthesis/', views.synth)

]