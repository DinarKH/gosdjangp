from django import forms
from django.forms import TextInput

from .models import RegistrationForm as RegForm

class RegistrationForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'pattern': '[A-Za-z0-9_]+','name':'Dimar'}))
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)
    home = forms.IntegerField(required=True)

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = RegForm
#         fields = ("name", "password","email","home")
