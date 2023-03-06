from django import forms
from .models import *
from erhanblog.base.models import Article

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
        

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image'   ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class UpdateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image'   ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }