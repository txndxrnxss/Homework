from django import forms


class LoginForm(forms.Form):
    nickname = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

