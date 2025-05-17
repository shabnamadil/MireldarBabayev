from django.core.files.uploadedfile import SimpleUploadedFile

from tests.utils.helpers import BaseDataMixin
from tests.utils.helpers.generate_file import (
    generate_dummy_file,
    generate_empty_docx_file,
)


class _FileValidationTest(BaseDataMixin):
    """
    Abstract class for FILE validation tests.
    Do not run directly.
    """

    def test_raises_validation_error_when_invalid_file_uploaded_with_disallowed_extension(
        self,
    ):
        fake_file = SimpleUploadedFile(
            name='invalid_file.txt',
            content=b'not an file at all',
            content_type='text/plain',
        )
        self.assert_invalid_data(self.object, 'file', fake_file)

    def test_raises_validation_error_when_empty_txt_file_uploaded(self):
        fake_file = SimpleUploadedFile(
            name='empty_file.txt', content=b'', content_type='text/plain'
        )
        self.assert_invalid_data(self.object, 'file', fake_file)

    def test_raises_validation_error_when_empty_pdf_file_uploaded(self):
        fake_file = SimpleUploadedFile(
            name='empty_file.pdf', content=b'', content_type='application/pdf'
        )
        self.assert_invalid_data(self.object, 'file', fake_file)

    def test_raises_validation_error_when_empty_docx_file_uploaded(self):
        fake_file = generate_empty_docx_file()
        self.assert_invalid_data(self.object, 'file', fake_file)

    def test_raises_validation_error_when_invalid_file_uploaded_with_pdf_extension(
        self,
    ):
        fake_file = SimpleUploadedFile(
            name='invalid_data.pdf',
            content=b'not an pdf at all',
            content_type='application/pdf',
        )
        self.assert_invalid_data(self.object, 'file', fake_file)

    def test_raises_validation_error_when_invalid_file_uploaded_with_docx_extension(
        self,
    ):
        fake_file = SimpleUploadedFile(
            name='invalid_data.docx',
            content=b'not an pdf at all',
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        )
        self.assert_invalid_data(self.object, 'file', fake_file)

    def test_raises_validation_error_when_valid_pdf_file_uploaded_with_disallowed_txt_extension(
        self,
    ):
        file = generate_dummy_file(file_type='pdf')
        fake_file = SimpleUploadedFile(name='valid_file.txt', content=file.read())
        self.assert_invalid_data(self.object, 'file', fake_file)

    def test_raises_validation_error_when_valid_docx_file_uploaded_with_disallowed_txt_extension(
        self,
    ):
        file = generate_dummy_file(file_type='docx')
        fake_file = SimpleUploadedFile(name='valid_file.txt', content=file.read())
        self.assert_invalid_data(self.object, 'file', fake_file)
