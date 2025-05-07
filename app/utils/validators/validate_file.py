from django.core.exceptions import ValidationError


def validate_extension(file_name, allowed_extensions=[".pdf", ".docx"]):
    if not any(file_name.lower().endswith(ext) for ext in allowed_extensions):
        raise ValidationError("Only PDF and DOCX files are accepted.")


def validate_type(file_name, file_type):
    if file_name.lower().endswith('.pdf') and file_type != 'pdf':
        raise ValidationError('File type does not match: expected PDF.')
    elif file_name.lower().endswith('.docx') and file_type != 'docx':
        raise ValidationError('File type does not match: expected DOCX.')
