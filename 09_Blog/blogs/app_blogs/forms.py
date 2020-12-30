from django import forms

from app_blogs.models import Post


class PostForm(forms.ModelForm):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Картинки', required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'files']
        widgets = {
            'body': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class PostFileUpload(forms.Form):
    file = forms.FileField(label='Файл *.csv')
