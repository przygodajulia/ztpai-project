# forms.py
from django import forms

class LoginForm(forms.Form):
    login_username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    login_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class RegisterForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    register_username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    location = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Location'}))
    register_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
