from django import forms
from django.forms import ModelForm
from .models import News, NewsComments


class NewsForm(ModelForm):

    class Meta:
        model = News
        fields = '__all__'


class NewsCommentsForm(ModelForm):

    class Meta:
        model = NewsComments
        fields = '__all__'
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'comment_text': forms.Textarea(attrs={'placeholder': 'Комментарий'}),
        }
