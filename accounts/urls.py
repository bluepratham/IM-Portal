from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views
urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$', views.register_profile),
    url(r'^edit_profile/$', views.edit_profile),
    url(r'^edit_userprofile/$', views.edit_UserProfile),
    url(r'^register_ironman/$', views.register_Ironman),
    url(r'^add_project/$', views.add_project),
    url(r'^evaluate/$',views.view_teams)

]
