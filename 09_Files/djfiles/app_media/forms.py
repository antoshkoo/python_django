from django import forms
from .models import File


class UploadDocumentForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['title', 'file']
