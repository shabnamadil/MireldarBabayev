from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import (
    SimpleUploadedFile,
)

from apps.service.models import Coworker
from utils.tests.base import BaseValidationTest


class TestCoworkerModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.coworker = Coworker.objects.create(
            name="Test coworker",
            png=SimpleUploadedFile(
                "test1.png",
                b"dummy png content",
                content_type="image/png",
            ),
        )

    def test_str_method(self):
        self.assert_str_method(self.coworker, "Test coworker")

    def test_unique_name(self):
        self.assert_unique_field(Coworker, "name", "Test coworker")

    def test_name_max_length(self):
        self.assert_max_length(self.coworker, "name", 100)

    def test_model(self):
        self.assert_model_instance(Coworker, "name", "Test coworker")
        self.assertTrue(self.coworker.png.name.startswith("coworkers/"))
        self.assertTrue(self.coworker.png.name.endswith("png"))

    def test_object_count(self):
        self.assert_object_count(Coworker, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(Coworker)

    def test_png_extension(self):
        self.coworker.png = "test/1.jpg"
        with self.assertRaises(ValidationError):
            self.coworker.full_clean()
