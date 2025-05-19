from unittest.mock import Mock, PropertyMock, patch

from apps.service.models import Download
from utils.tests.base import BaseValidationTest


class TestDownloadModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.model = Download

    def test_download_str_returns_title(self):
        self.assert_str_output(self.model, 'title', 'Test title')

    def test_file_size_property_returns_correct_size(self):
        mock_file = Mock()
        mock_file.size = 2048  # 2 KB

        download = self.model()
        download.file = mock_file

        self.assertEqual(download.file_size, 2048)

    def test_file_size_formatted_kb(self):
        download = self.model()

        with patch.object(
            self.model, 'file_size', new_callable=PropertyMock
        ) as mock_file_size:
            mock_file_size.return_value = 2048  # 2 KB
            self.assertEqual(download.file_size_formatted, "2.00 KB")

    def test_file_size_formatted_mb(self):
        download = self.model()

        with patch.object(
            self.model, 'file_size', new_callable=PropertyMock
        ) as mock_file_size:
            mock_file_size.return_value = 5 * 1024 * 1024  # 5 MB
            self.assertEqual(download.file_size_formatted, "5.00 MB")

    def test_file_size_formatted_bytes(self):
        download = self.model()

        with patch.object(
            self.model, 'file_size', new_callable=PropertyMock
        ) as mock_file_size:
            mock_file_size.return_value = 512  # 512 bytes
            self.assertEqual(download.file_size_formatted, "512.00 B")
