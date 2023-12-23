from django import forms
from .models import Profile, Report

"""class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']
        #labels = {'text': 'Comment'}
        widgets = {
            'photo': forms.ImageField(attrs={
                'class': 'rounded_list',
                'placeholder': 'Choose file:',
            })
        }"""


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'city', 'birth_date', 'lang', ]
        #'avatar'

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['text']
