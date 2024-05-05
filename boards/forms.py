from django import forms 
from .models import Comment, Card, List, Board 

class Boardform(forms.ModelForm):  
    class Meta:
        model = Board
        fields = ['title']


class BoardForm(forms.ModelForm):
    
    class Meta:
        model = Board
        fields = ['title']


class CardForm(forms.ModelForm):
    
    class Meta:
        model = Card
        fields = ['title', 'description', 'opened_by', 'assigned_to', 'labels']

        widgets= {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'opened_by':forms.Select(attrs={'class':'form-control'}),
            'assign_to':forms.Select(attrs={'class':'form-control'}),
            'list':forms.HiddenInput(),
            'assigned_to': forms.CheckboxSelectMultiple
            
        }


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['text']

