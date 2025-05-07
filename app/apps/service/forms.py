from django import forms

from utils.validators.validate_file import (
    validate_extension,
    validate_type,
)

from .models import Download


class DownloadBaseForm(forms.ModelForm):
    class Meta:
        model = Download
        fields = '__all__'

    def clean_file(self):
        cleaned_data = super().clean()
        file = cleaned_data.get('file')
        file_type = cleaned_data.get('type')

        if file:
            validate_extension(file.name)
            validate_type(file.name, file_type)
        return cleaned_data
