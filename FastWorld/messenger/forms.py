from .models import Message
from django.forms import ModelForm, TextInput, Textarea

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Message text:',
            })
        }