from django import forms
from .models import *
from tinymce.widgets import TinyMCE

class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['description', 'adminurl', 'username', 'password', 'extra_credential']
        widgets = {
            'description' : TinyMCE(attrs={'cols': 80, 'rows': 10}),
            'extra_credential' : TinyMCE(attrs={'cols': 80, 'rows': 10}),
            'password' : forms.TextInput(attrs={'class' : 'form-control'}),
            'adminurl' : forms.TextInput(attrs={'class' : 'form-control'}),
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
        }