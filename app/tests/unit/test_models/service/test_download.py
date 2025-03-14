from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import IntegrityError

from apps.service.forms import DownloadBaseForm
from apps.service.models import Download, Service
from utils.tests.base import BaseValidationTest


class TestDownloadModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.service = Service.objects.create(name='Test service')
        cls.file_content = b"dummy file content" * 1024
        cls.object = Download.objects.create(
            title='Test download',
            type='pdf',
            file=SimpleUploadedFile(
                "test.pdf",
                b"dummy file content",
                content_type="application/pdf",
            ),
            service=cls.service,
        )

    def test_str_method(self):
        self.assert_str_method(self.object, 'Test download')

    def test_title_max_length(self):
        self.assert_max_length(self.object, 'title', 100)

    def object_count(self):
        self.assert_object_count(Download, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(Download)

    def test_model(self):
        self.assert_model_instance(Download, 'title', 'Test download')
        self.assert_model_instance(Download, 'type', 'pdf')
        self.assert_model_instance(Download, 'service', self.service)
        self.assertTrue(
            self.object.file.name.startswith('services/downloads/test')
        )
        self.assertTrue(self.object.file.name.endswith('pdf'))

    def test_unique_together(self):
        object = Download(
            title='Test download',
            type='pdf',
            file=SimpleUploadedFile(
                "test.pdf",
                b"dummy file content",
                content_type="application/pdf",
            ),
            service=self.service,
        )

        with self.assertRaises(IntegrityError):
            object.save()

    def test_invalid_file_type_via_form(self):
        data = {
            'title': 'Test download invalid',
            'type': 'pdf',
            'service': self.service.pk,
        }
        files = {
            'file': SimpleUploadedFile(
                "test.jpg", b"dummy jpg content", content_type="image/jpeg"
            )
        }
        form = DownloadBaseForm(data=data, files=files)
        self.assertFalse(form.is_valid())
        self.assertIn('file', form.errors)

    def test_invalid_unity_file_type(self):
        data = {
            'title': 'Test download invalid',
            'type': 'pdf',
            'service': self.service.pk,
        }
        files = {
            'file': SimpleUploadedFile(
                "test.docx",
                b"dummy docx content",
                content_type="application/docx",
            )
        }

        form = DownloadBaseForm(data=data, files=files)
        self.assertFalse(form.is_valid())
        self.assertIn('file', form.errors)

    def test_file_size(self):
        expected_size = len(self.file_content)
        object_size = self.object.file_size * 1024
        self.assertEqual(object_size, expected_size)

    def test_file_size_large_file(self):
        """Test for a large file in MB"""
        large_content = b"x" * (10 * 1024 * 1024)  # Exactly 10 MB
        large_file = SimpleUploadedFile(
            "large.pdf", large_content, content_type="application/pdf"
        )
        large_download = Download.objects.create(
            title="Large File",
            type="pdf",
            file=large_file,
            service=self.service,
        )

        self.assertEqual(large_download.file_size, len(large_content))
        self.assertEqual(
            large_download.file_size_formatted,
            f"{len(large_content) / (1024 * 1024):.2f} MB",
        )

    def test_file_size_formatted(self):
        """Test that file_size_formatted returns human-readable format"""
        self.object = Download.objects.create(
            title="Test File",
            type="pdf",
            file=SimpleUploadedFile(
                "test.pdf", self.file_content, content_type="application/pdf"
            ),
            service=self.service,
        )

        expected_size_bytes = len(
            self.file_content
        )  # Get actual size in bytes
        formatted_size = self.object.file_size_formatted

        if expected_size_bytes < 1024:
            self.assertEqual(
                formatted_size, f"{expected_size_bytes:.2f} B"
            )  # Expect bytes
        else:
            expected_size_kb = expected_size_bytes / 1024
            self.assertEqual(formatted_size, f"{expected_size_kb:.2f} KB")
