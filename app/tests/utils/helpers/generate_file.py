from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile

from docx import Document


def generate_dummy_file(file_type):
    if file_type == 'pdf':
        return SimpleUploadedFile(
            "example.pdf", b"%PDF-1.4 dummy pdf content", content_type="application/pdf"
        )
    elif file_type == 'docx':
        return SimpleUploadedFile(
            "example.docx",
            b"PK\x03\x04 dummy docx content",
            content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )


def generate_empty_docx_file():
    docx_buffer = BytesIO()
    Document().save(docx_buffer)
    docx_buffer.seek(0)
    return SimpleUploadedFile(
        name='empty.docx',
        content=docx_buffer.read(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    )
