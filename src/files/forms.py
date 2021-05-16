from django import forms
from files.models import Upload


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('fileName', 'info', 'document')
