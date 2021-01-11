from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import Form


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class UserRestorePasswordForm(Form):
    email = forms.EmailField()
