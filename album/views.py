from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import Album, Song
from django.core.urlresolvers import reverse
# Create your views here.

def home(request):

    return render(request, 'album/home.html' )

class create(CreateView):
    model = Album
    template_name = 'album/add_album.html'
    fields = ['title','artist']

    def get_success_url(self):
        return reverse('album-home')

class album(DetailView):

    model = Album