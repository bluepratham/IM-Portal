from django.shortcuts import render, HttpResponse, redirect, Http404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import (Registration, editProfile,
                    UserProfileForm, IronManForm,
                    FolderForm, EvaluationForm)
from .models import Folder, Project, IronMan
from django.contrib.auth.models import User
from ironman.models import ShareDoc
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework import response,status
from .serializers import IronManSerializer
# Create your views here.


def home(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return redirect('/admin/')
        elif request.user.groups.all()[0].name == 'ironmen':
            projects = Folder.objects.filter(team=request.user)
            return render(request, 'accounts/home.html',
                          {'projects':projects})
        else:
            # return render(request, 'accounts/home.html')
            teams = Folder.objects.filter(client=request.user)

            return render(request, 'accounts/viewTeams.html', {'teams': teams})
    else:
        return redirect('/account/login/')
    # try:
    #
    #
    # except:
    #     raise Http404()


def register_profile(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/account")
        else:
            form = Registration()
            return render(request, 'accounts/register.html', {'form': form})

    else:
        form = Registration()
        return render(request, 'accounts/register.html' , {'form':form})

def edit_profile(request):
    if request.method == "POST":
        form = editProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            redirect('/account/profile/')
    else:

        form = editProfile(instance=request.user)
        return render(request, 'accounts/edit.html', {'form': form})

def edit_UserProfile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            redirect('/accounts/')


    else:
        form = UserProfileForm(instance=request.user.userprofile)
        return render(request, 'accounts/edit.html', {'form': form})

def register_Ironman(request):
    if request.method == "POST":
        form = IronManForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = IronManForm()
        return render(request, 'accounts/register.html', {'form': form} )

def add_project(request):
    if request.method == "POST":
        form = FolderForm(request.POST)
        if form.is_valid():
            print('form is valid')
            forms = form.save(commit=False)
            forms.team = request.user
            forms.save()
            return redirect('/account/')
    else:
        form = FolderForm()
        return render(request, 'accounts/register.html', {'form':form})


def view_teams(request):
    teams = Folder.objects.filter(client= request.user)
    return render(request, 'accounts/viewTeams.html', {'teams':teams})

@login_required
def evaluate(request, projID, teamName):
    if request.method == "POST":
        form = EvaluationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.client = request.user
            form.project = Project.objects.get(id=projID)
            form.team = User.objects.get(username=teamName)
            form.save()
            folder = Folder.objects.get(client=request.user,
                                        team=User.objects.get(username=teamName),
                                        project=Project.objects.get(id=projID))
            folder.is_active = False
            folder.save()
            return HttpResponse("Evaluations Saved")
    else:
        form = EvaluationForm()
        object = Folder.objects.get(team = User.objects.get(username=teamName), project = Project.
                objects.get(id=projID), client=request.user)
        prob = object.prob_stat
        is_active = object.is_active
        shareditems = ShareDoc.objects.filter(team = User.objects.get(username=teamName),
                                              project = Project.objects.get(id=projID))
        print(shareditems)
        return render(request, 'accounts/teamDetail.html', {'form':form,'prob':prob,
                                                          'shared':shareditems,'is_active':is_active})


class IronmanAPI(APIView):
    print('aaaaaaaaa1')
    def get(self,request):
       print('aaaaaaaaa')
       ironman =  IronMan.objects.all()
       serializer = IronManSerializer(ironman,many=True)
       return response.Response(serializer.data)

    def post(self):
        pass