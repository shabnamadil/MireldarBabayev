from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import (
    SimpleUploadedFile,
)

from apps.core.models import Banner
from utils.tests.base import BaseValidationTest


class TestBannerModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.banner = Banner.objects.create(
            title="Banner title",
            subtitle="Banner subtitle",
            description="Banner description",
            png=SimpleUploadedFile(
                "test1.png",
                b"dummy png content",
                content_type="image/png",
            ),
            video_id="MKG_6BqnhpI",
        )

    def test_banner_model(self):
        self.assert_model_instance(Banner, "title", "Banner title")
        self.assert_model_instance(Banner, "subtitle", "Banner subtitle")
        self.assert_model_instance(
            Banner,
            "description",
            "Banner description",
        )
        self.assert_model_instance(Banner, "video_id", "MKG_6BqnhpI")
        self.assertTrue(self.banner.png.name.startswith("banner/"))
        self.assertTrue(self.banner.png.name.endswith("png"))

    def test_str_method(self):
        self.assert_str_method(self.banner, "Banner title")

    def test_title_unique(self):
        self.assert_unique_field(Banner, "title", "Banner title")

    def test_subtitle_unique(self):
        self.assert_unique_field(Banner, "subtitle", "Banner subtitle")

    def test_description_unique(self):
        self.assert_unique_field(
            Banner,
            "description",
            "Banner description",
        )

    def test_video_id_unique(self):
        self.assert_unique_field(Banner, "video_id", "MKG_6BqnhpI")

    def test_fields_max_length(self):
        self.assert_max_length(self.banner, "video_id", 11)
        self.assert_max_length(self.banner, "title", 100)
        self.assert_max_length(self.banner, "subtitle", 100)

    def test_png_file_extension(self):
        self.banner.png.name = "banner/1.jpg"
        with self.assertRaises(ValidationError):
            self.banner.full_clean()

    def test_object_count(self):
        self.assert_object_count(Banner, 1)

    def test_deletion(self):
        self.assert_object_deleted(Banner)
