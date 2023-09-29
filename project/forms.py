from django import forms
from .models import *
from tinymce.widgets import TinyMCE
from ckeditor.widgets import CKEditorWidget

class ProjectEditForm(forms.ModelForm):
    #description = forms.CharField(widget = CKEditorWidget())
    #extra_credential = forms.CharField(widget = CKEditorWidget())

    class Meta:
        model = Project
        fields = ['description', 'adminurl', 'username', 'password', 'extra_credential']
        
        widgets = {
            'description' : forms.Textarea(attrs={'class': 'ckeditor form-control'}),
            'password' : forms.TextInput(attrs={'class' : 'form-control'}),
            'adminurl' : forms.TextInput(attrs={'class' : 'form-control'}),
            'username' : forms.TextInput(attrs={'class' : 'form-control'}),
        }