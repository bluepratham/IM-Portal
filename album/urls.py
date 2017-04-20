from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.home ,name='album-home'),
    url(r'^add/$', views.create.as_view(), name='add-album'),
    url(r'albums(?P<pk>\d)/$', views.album.as_view(), name='all-album') #detailview needs pk/slug passed in from url
]