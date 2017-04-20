from django.shortcuts import (render, HttpResponse,
                              redirect, HttpResponseRedirect)
from datetime import datetime
from accounts.models import Project, Product, Folder
# Create your views here.
from django.contrib.auth.models import User
from .forms import (ScrumForm, SessReqForm,
                    BugForm, ShareDocForm, SynthesisForm)
from .models import (Scrum, SessionReq,
                     synthesis,Bug)
def ironmanHome(request):
    user = request.user
    scrums = Scrum.objects.filter(created_by = user)
    return render(request, 'ironmanHome.html', {'scrums':scrums})

def req_session(request, id):
    form = SessReqForm()

    if request.method != "POST":
        print(id)
        sessions = SessionReq.objects.filter(
            project=Project.objects.get(id=id))
        context = {'form':form, 'sessions' : sessions }
        return render( request,'scrumForm.html', context )
    if request.method == "POST":
        a = SessReqForm(request.POST)
        if a.is_valid:
            a = a.save(commit = False)
            a.date = str(datetime.now().date())
            a.project  = Project.objects.get(id=id)
            a.save()
        return HttpResponse("Session Request Submitted")

def contact(request):
    return render(request, 'contacts.html' )


def project(request,projNum):
    print(request.method)
    scrumform = ScrumForm()
    bugform = BugForm()
    sessionform = SessReqForm()
    shareform = ShareDocForm()
    sessions = SessionReq.objects.filter(
        project=Project.objects.get(id=projNum))
    if request.method == "GET":
        prob_stat = Folder.objects.get(project=Project.objects.get(id=projNum),
                                  team=request.user).prob_stat
        print(prob_stat)
        scrums = Scrum.objects.filter(created_by=request.user)
        context = {'scrumform': scrumform, 'scrums':scrums,
                   'bugform': bugform ,'shareform':shareform,
                   'sessionform':sessionform ,'sessions':sessions ,
                   'projNum':projNum, 'prob_stat':prob_stat}
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

def req_bug(request,a):
    if request.method == "POST":
        form = BugForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.team = request.user
            form.save()
            return HttpResponse('Your report was raised, Thanks')
    else:
        form = BugForm()
        return render(request, 'scrumForm.html',{
            'form' : form
        } )

def share(request, projID, teamName):
    if request.method == "GET":
        form = ShareDocForm()
        return render(request, 'scrumForm.html', {'form':form})
    elif request.method == "POST":
        form = ShareDocForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.team = User.objects.get(username=teamName)
            form.project = Project.objects.get(id = projID)
            form.save()
            return HttpResponse("Sent to Client")


from django.views.generic import ListView, DetailView
from django.shortcuts import get_list_or_404, get_object_or_404

class scrumlist(ListView):
    model = Scrum
    template_name = 'listview.html'
    context_object_name = 'scrumlist'
    # queryset = Scrum.objects.filter(created_by=request.user)
    s = 'was'

    def get_queryset(self):
        print(self.kwargs['name'])
        return get_list_or_404(Scrum.objects.filter(created_by = self.request.user))

class scrumview(DetailView):
    model = Scrum

    def get_object(self):
        return get_object_or_404(Scrum.objects.get(id=1))

def synth(request):
    pass
#TODO: scrum listview is done, make detailview for it with proper href in list view
#TODO: check what is @property decorator (suggested by pycharm)