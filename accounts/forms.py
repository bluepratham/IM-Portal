from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, IronMan, Folder, Evaluate

class Registration(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name' ,  'groups')

    def save(self, commit = True):
        user = super(Registration,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()


class editProfile(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password'
        ]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'description', 'city']

class IronManForm(forms.ModelForm):
    class Meta:
        model = IronMan
        fields = ['username', 'first_name',
                  'mid_name', 'last_name']


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['project', 'client']

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluate
        fields = ['performance','attitude']