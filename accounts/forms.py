from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class Registration(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name' ,  'is_active')

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