from django import forms

from .models import File


class UploadPriceForm(forms.Form):
    file = forms.FileField()


class UploadDocumentForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['title', 'file']
