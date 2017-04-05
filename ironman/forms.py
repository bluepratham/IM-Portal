from django import forms
from .models import Scrum

class ScrumForm(forms.ModelForm):
    class Meta:
        model = Scrum
        fields = [
            'comp_yest' ,
        'roadblk' ,
        'plan_tdy',
        'learning'
        ]