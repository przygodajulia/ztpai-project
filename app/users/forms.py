# forms.py
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class RegisterForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

