from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, min_length=4)
    password1 = forms.CharField(widget=forms.PasswordInput(), min_length=3)
    password2 = forms.CharField(widget=forms.PasswordInput(), min_length=3)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, min_length=4)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=3)
