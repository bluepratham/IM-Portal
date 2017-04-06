from django import forms
from ironman.models import Scrum, SessionReq

class ScrumForm(forms.ModelForm):
    class Meta:
        model = Scrum
        fields = [
            'comp_yest' ,
        'roadblk' ,
        'plan_tdy',
        'learning'
        ]

class requestForm(forms.ModelForm):
    class Meta:
        model = SessionReq
        fields = [
            'SessionOn',
            'Details'
        ]