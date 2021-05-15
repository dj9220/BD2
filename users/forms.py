from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Message, Profile



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['sender', ]
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['user', ]
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',

    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password'
    }))