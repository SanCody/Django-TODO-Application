from django import forms
from .models import taskData
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class data(forms.ModelForm):
    class Meta:
        model = taskData
        fields = ['task','desc']

class RegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class":"form-control"
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "class":"form-control"
    }))
    password1 = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "id":"Rpassword"
    }))
    password2 = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput(attrs={
        "class":"form-control"
    }))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        'autocomplete': 'on'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        'autocomplete': 'on'
    }))