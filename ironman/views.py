from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from accounts.models import Project
# Create your views here.

from .forms import ScrumForm, SessReqForm
from .models import Scrum, SessionReq, synthesis
def ironmanHome(request):
    user = request.user
    scrums = Scrum.objects.filter(created_by = user)
    return render(request, 'ironmanHome.html', {'scrums':scrums})

# def Scrum_Create(request):
#     print(request.method)
#     form = ScrumForm()
#     if request.method == "GET":
#         context = {'form':form}
#         return render(request, 'scrumForm.html', context)
#     if request.method == "POST":
#         a = ScrumForm(request.POST)
#         if a.is_valid:
#             print(a.is_valid)
#             a = a.save(commit = False)
#             a.date = str(datetime.now().date())
#             a.created_by = str(request.user.username)
#             a.save()
#             print(request.user)
#         return HttpResponse("Scrum Saved")


def req_session(request, id):
    form = SessReqForm()

    if request.method != "POST":
        print(id)
        sessions = SessionReq.objects.filter(
            project=Project.objects.get(id=id))
        context = {'form':form, 'sessions' : sessions }
        return render( request,'scrumForm.html', context )
    if request.method == "POST":
        a = requestForm(request.POST)
        if a.is_valid:
            a = a.save(commit = False)
            a.date = str(datetime.now().date())
            a.save()
        return HttpResponse("Your Request Submitted. We will fulfill it ASAP")

def contact(request):
    return render(request, 'contacts.html' )

from django.template import Template, Context
def synth(request):
    context = {'model': synthesis.objects.all()}
    temp = Template(" {% for object in model%}{{object.content}}{% endfor %}")
    return HttpResponse(temp.render(Context(context)))

def project(request,projNum):
    print(request.method)
    form = ScrumForm()
    if request.method == "GET":
        scrums = Scrum.objects.filter(created_by=request.user)
        context = {'form': form, 'scrums':scrums, 'projNum':projNum}
        return render(request, 'scrumForm.html', context)
    if request.method == "POST":
        a = ScrumForm(request.POST)
        if a.is_valid():
            print(a.is_valid)
            a = a.save(commit=False)
            a.date = str(datetime.now().date())
            a.created_by = str(request.user.username)
            a.project = Project.objects.get(id=projNum)
            a.save()
            print(request.user)
        return redirect("/ironman/" + str(projNum))