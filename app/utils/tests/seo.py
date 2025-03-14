from django.core.files.uploadedfile import SimpleUploadedFile

from .base import BaseValidationTest


class BaseSeoTest(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.valid_data = {
            "meta_title": "This is a valid SEO Title",
            "meta_description": "This is a valid meta description within the required length range.",
            "meta_keywords": "keyword1, keyword2, keyword3, keyword4",
            "og_title": "This is a valid OG Title",
            "og_description": "This is a valid OG description for testing SEO constraints.",
            "og_image": SimpleUploadedFile(
                name="test_image.jpg",
                content=b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01",
                content_type="image/jpeg",
            ),
        }
