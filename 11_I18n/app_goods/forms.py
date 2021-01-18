from django import forms
from django.utils.translation import gettext_lazy as _


class UploadPriceFileForm(forms.Form):
    file = forms.FileField(label=_('File *.csv'))
