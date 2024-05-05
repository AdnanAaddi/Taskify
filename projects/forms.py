from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description','collaborators']

        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            'collaborators': forms.SelectMultiple(attrs={'class':'form-control'}),
        }

class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'collaborators']

        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            'collaborators': forms.SelectMultiple(attrs={'class':'form-control'}),
        }
        


        