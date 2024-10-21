from django import forms
from .models import S3File

class S3FileUploadForm(forms.ModelForm):
    class Meta:
        model = S3File
        fields = ['file']

    def clean_file(self):
        uploaded_file = self.cleaned_data['file']
        # You can validate file types, size, etc. here
        return uploaded_file
