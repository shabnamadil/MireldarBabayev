from django import forms
from django.core.exceptions import ValidationError

from .models import Download


class DownloadBaseForm(forms.ModelForm):
    class Meta:
        model = Download
        fields = "__all__"

    def clean_file(self):
        cleaned_data = super().clean()
        file = cleaned_data.get("file")
        file_type = cleaned_data.get("type")

        if file:
            # Validate file extension
            if not (
                file.name.lower().endswith(".pdf")
                or file.name.lower().endswith(".docx")
            ):
                raise ValidationError("Only PDF or DOCX files are accepted.")

            # Check that file type matches the `type` field
            if file.name.lower().endswith(".pdf") and file_type != "pdf":
                raise ValidationError(
                    "File type does not match: expected PDF."
                )
            elif file.name.lower().endswith(".docx") and file_type != "docx":
                raise ValidationError(
                    "File type does not match: expected DOCX."
                )

        return cleaned_data
