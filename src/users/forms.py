from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    username = forms.CharField(label="username", min_length=8, max_length=30)
    first_name = forms.CharField(label="First name", min_length=2, max_length=50)
    last_name = forms.CharField(label="Last name", max_length=100)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        label="first_name", min_length=3, max_length=25, required=False
    )
    last_name = forms.CharField(
        label="last_name", min_length=2, max_length=50, required=False
    )
    username = forms.CharField(label="username", min_length=5, max_length=150)
    email = forms.EmailField(label="email")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]


class XTBLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
