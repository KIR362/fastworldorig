from .models import Articles, Comments
from django.forms import ModelForm, TextInput, Textarea
from django import forms

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'intro', 'full_text']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title:',
            }),
            'intro': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Intro:',
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text:',
            })
        }

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        #labels = {'text': 'Comment'}
        widgets = {
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Comment text:',
            })
        }
