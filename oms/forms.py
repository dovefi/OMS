from django import forms

class UserForm(forms.Form):
    user_name = forms.CharField(max_length=11)
    user_email = forms.EmailField(required=True, max_length=30)
    user_password = forms.CharField(max_length=15)