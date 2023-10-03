from django import forms
from .models import *

class TaskAddForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created_at']
    
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'project' : forms.Select(attrs={'class' : 'form-control'}),
            'assigned_to' : forms.Select(attrs={'class' : 'form-control'}),
            'priority' : forms.Select(attrs={'class' : 'form-control'}),
            'status' : forms.Select(attrs={'class' : 'form-control'}),
            'files' : forms.ClearableFileInput(attrs={'multiple' : True}),
        }