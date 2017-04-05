from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import Scrum
# Create your views here.

from .forms import ScrumForm

def ironmanHome(request):
    return HttpResponse('you are <br> <a href ="add_scrum/"> add scrum</a> ')

def Scrum_Create(request):
    print(request.method)
    form = ScrumForm()

    if request.method == "GET":

        context = {'form':form}
        return render(request, 'scrumForm.html', context)
    if request.method == "POST":
        a = ScrumForm(request.POST)
        if a.is_valid:
            a = a.save(commit = False)
            a.date = str(datetime.now().date())
            a.created_by = str(request.user.username)
            a.save()
            print(request.user)

        return HttpResponse("Scrum Saved")
