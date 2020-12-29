from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserProfileForm(UserChangeForm):
    password = None
    email = None

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

