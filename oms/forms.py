from django import forms
from .models import OmsUser
from django.contrib.auth.forms import AuthenticationForm

__all__ = ['UserCreateUpdateForm','UserLoginForm']


class UserCreateUpdateForm(forms.ModelForm):

    class Meta:
        model = OmsUser
        fields = [
            'username', 'email', 'password'
        ]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True)

    class Meta:
        fields = ['username', 'password']
