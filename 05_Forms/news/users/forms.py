from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=False, help_text='Ваше имя')
    last_name = forms.CharField(max_length=20, required=False, help_text='Ваша Фамилия')
    email = forms.EmailField(required=True, help_text='Email')
    city = forms.CharField(max_length=30, required=False, help_text='Город')
    phone = forms.IntegerField(required=False, help_text='Телефон')
    date_of_birth = forms.DateField(required=False, help_text='Дата Рождения')
    discount_card = forms.IntegerField(required=False, help_text='Карта')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ваша фамилия'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }
