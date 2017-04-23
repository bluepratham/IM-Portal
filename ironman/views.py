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
    scrumform = ScrumForm()
    bugform = BugForm()
    sessionform = SessReqForm()
    shareform = ShareDocForm()
    sessions = SessionReq.objects.filter(
        project=Project.objects.get(id=projNum))
    if request.method == "GET":
        obj = Folder.objects.get(project=Project.objects.get(id=projNum),
                                  team=request.user)
        prob_stat = obj.prob_stat
        is_active = obj.is_active
        scrums = Scrum.objects.filter(created_by=request.user)
        context = {'scrumform': scrumform, 'scrums':scrums,
                   'bugform': bugform ,'shareform':shareform,
                   'sessionform':sessionform ,'sessions':sessions ,
                   'projNum':projNum, 'prob_stat':prob_stat,
                   'is_active': is_active}
        return render(request, 'scrumForm.html', context)
    if request.method == "POST":
        a = ScrumForm(request.POST)
        print(request.POST)
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
        print(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.team = User.objects.get(username=teamName)
            form.project = Project.objects.get(id = projID)
            # form.text = request.POST['content']
            form.save()
            return HttpResponse("Sent to Client")


from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_list_or_404, get_object_or_404

class scrumlist(ListView):
    model = Scrum
    template_name = 'listview.html'
    context_object_name = 'scrumList'
    # queryset = Scrum.objects.filter(created_by=request.user)
    s = 'was'

    def get_queryset(self):
        print(self.kwargs['name'])
        object =  get_list_or_404(Scrum.objects.filter(created_by = self.request.user))
        print(object)
        return object

class scrumview(DetailView):
    model = Scrum

    def get_object(self):
        return get_object_or_404(Scrum.objects.get(id=1))

class SynthesisList(ListView):
    model = synthesis
    template_name = "listview.html"
    context_object_name = 'synthesisList'
    synthesisform = SynthesisForm()


class SynthesisDetail(DetailView):
    model = synthesis

def SynthesisCreate(request):
    form = SynthesisForm()
    if request.method == "POST":
        form = SynthesisForm(request.POST)
        form = form.save(commit=False)
        form.team = request.user
        form.save()
        return HttpResponseRedirect("/ironman/synthesis/")
    elif request.method == "GET":
        return render(request, 'ironman/synthesis_form.html', {'form':form})


#TODO: scrum listview is done, make detailview for it with proper href in list view

def vote(request,pk):
    if request.method=="POST":
        for id in request.POST.getlist('sessionID'):
            session = SessionReq.objects.get(id=id)
            session.votes.add(request.user)
            # session.votes.update(request.user)
        return HttpResponseRedirect('/ironman/'+pk)