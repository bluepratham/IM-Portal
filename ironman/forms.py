from django import forms
from ironman.models import (
    Scrum, SessionReq, Bug, ShareDoc, synthesis)
from tinymce.widgets import TinyMCE


class ScrumForm(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 40}))
    class Meta:
        model = Scrum
        fields = [
            'comp_yest' ,
        'roadblk' ,
        'plan_tdy',
        'learning'
        ]

class SessReqForm(forms.ModelForm):
    class Meta:
        model = SessionReq
        fields = [
            'SessionOn',
            'Details'
        ]

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = [
            'txt','que','prod'
        ]

class ShareDocForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 40}))
    class Meta:
        model = ShareDoc
        fields = ['text']

class SynthesisForm(forms.ModelForm):

    class Meta:
        model = synthesis
        fields = ['heading', 'content',
                  'source', 'by']