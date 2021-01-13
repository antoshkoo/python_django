from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import Form, ModelForm

from app_users.models import Profile


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['about', 'avatar']


class UserRestorePasswordForm(Form):
    email = forms.EmailField()
