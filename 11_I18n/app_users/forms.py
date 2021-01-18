from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import SelectDateWidget
from django.utils.translation import gettext_lazy as _

from app_users.models import User


class AuthForm(forms.Form):
    username = forms.CharField(label=_('Your name'))
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'))


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label=_('First name'))
    last_name = forms.CharField(max_length=30, required=False, label=_('Last name'))
    date_of_birth = forms.DateField(required=False, label=_('Date of birth'),
                                    widget=SelectDateWidget(years=range(1910, 2020)))
    city = forms.CharField(max_length=30, required=False, label=_('City'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    file = forms.FileField()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class RestorePasswordForm(forms.Form):
    email = forms.EmailField()

