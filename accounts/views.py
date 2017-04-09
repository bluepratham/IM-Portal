from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import Registration, editProfile, UserProfileForm
# Create your views here.


def home(request):
    lst = [1, 2, 3, 4, 5]
    name = 'pratham'
    return render(request, 'accounts/home.html', {'list': lst,
                                                   'name': name})


def register_profile(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/account")
        else:
            form = Registration()
            return render(request, 'accounts/login.html', {'form': form})

    else:
        form = Registration()
        return render(request, 'accounts/login.html' , {'form':form})

def edit_profile(request):
    if request.method == "POST":
        form = editProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            redirect('/account/profile/')
    else:
        print("adadasdadadad")
        form = editProfile(instance=request.user)
        return render(request, 'accounts/login.html', {'form': form})

def edit_UserProfile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            redirect('/accounts/')


    else:
        form = UserProfileForm(instance=request.user.userprofile)
        return render(request, 'accounts/login.html', {'form': form})
