from django.core.exceptions import ValidationError
from django.db import IntegrityError

from apps.service.models import Download
from tests.utils.factories import DownloadFactory
from tests.utils.helpers import _FileValidationTest, generate_dummy_file
from utils.tests.base import BaseValidationTest


class DownloadModelIntegration(BaseValidationTest, _FileValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.object = DownloadFactory()

    def test_title_required(self):
        self.assert_required_field(self.object, 'title')

    def test_type_required(self):
        self.assert_required_field(self.object, 'type')

    def test_file_required(self):
        self.assert_required_field(self.object, 'file')

    def test_object_count(self):
        self.assert_object_count(Download, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(Download)

    def test_download_title_saved_correctly(self):
        self.assert_model_instance(self.object, 'title', self.object.title)

    def test_download_title_gets_file_main_name(self):
        fake_file = generate_dummy_file('pdf')
        download = DownloadFactory(file=fake_file)
        self.assertTrue(fake_file.name, download.title)

    def test_download_file_type_saved_correctly(self):
        self.assert_model_instance(self.object, 'type', self.object.type)

    def test_download_file_saved_correctly(self):
        self.assertTrue(self.object.file.name.startswith('services/downloads'))

    def test_raises_validation_error_when_invalid_file_type_choices(self):
        download = DownloadFactory.build(type='invalid_choice')
        with self.assertRaises(ValidationError):
            download.full_clean()

    def test_file_pdf_extension_saved_correctly(self):
        download = DownloadFactory.build(type='pdf')
        self.assertTrue(download.file.name.endswith('pdf'))

    def test_file_docx_extension_saved_correctly(self):
        download = DownloadFactory.build(type='docx')
        self.assertTrue(download.file.name.endswith('docx'))

    def test_object_is_instance_of_download(self):
        self.assertIsInstance(self.object, Download)

    def test_downloads_are_ordered_by_created_at_desc(self):
        self.assert_ordering(DownloadFactory, Download)

    def test_unique_together(self):
        download = DownloadFactory.build(
            title=self.object.title,
            service=self.object.service,
        )

        with self.assertRaises(IntegrityError):
            download.save()

    def test_service_returns_none_when_no_added(self):
        download = DownloadFactory(service=None)
        self.assertIsNone(download.service)
