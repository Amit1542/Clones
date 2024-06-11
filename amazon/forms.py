from django import forms
from .models import *

class signupForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    Confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model= signup
        widget = {
        'Password': forms.PasswordInput(),
    }
        fields="__all__"
