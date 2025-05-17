from io import BytesIO

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from docx import Document
from PyPDF2 import PdfReader


def validate_extension(file_name, allowed_extensions=[".pdf", ".docx"]):
    if not any(file_name.lower().endswith(ext) for ext in allowed_extensions):
        raise ValidationError(_("Only PDF and DOCX files are accepted."))


def validate_type(file_name, file_type):
    if file_name.lower().endswith('.pdf') and file_type != 'pdf':
        raise ValidationError(_('File type does not match: expected PDF.'))
    elif file_name.lower().endswith('.docx') and file_type != 'docx':
        raise ValidationError(_('File type does not match: expected DOCX.'))


def validate_pdf_content(file):
    try:
        reader = PdfReader(BytesIO(file.read()))
        file.seek(0)  # Reset for later use
        if not reader.pages:
            raise ValidationError(_("The uploaded PDF file is empty."))
    except Exception:
        raise ValidationError(_("The uploaded file is not a valid PDF."))


def validate_docx_content(file):
    try:
        document = Document(file)
        file.seek(0)  # Reset for later use
        if not any(p.text.strip() for p in document.paragraphs):
            raise ValidationError(_("The uploaded DOCX file is empty."))
    except Exception:
        raise ValidationError(_("The uploaded file is not a valid DOCX document."))


def validate_file_content(file, expected_type):
    ext = file.name.lower().split('.')[-1]

    # Ensure we reset the file pointer before reading
    file.seek(0)

    if ext == 'pdf' and expected_type == 'pdf':
        validate_pdf_content(file)

    elif ext == 'docx' and expected_type == 'docx':
        validate_docx_content(file)

    else:
        raise ValidationError(
            _("Unsupported file type or mismatch with selected type.")
        )
