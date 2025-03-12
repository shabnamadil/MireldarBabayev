from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import (
    SimpleUploadedFile,
)
from django.db import IntegrityError

from apps.seo.models import ServiceDetailPageSeo
from apps.service.models import Service
from utils.tests.seo import BaseValidationTest


class TestServiceDetailPageSeoModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.model = ServiceDetailPageSeo

        cls.service, _ = Service.objects.get_or_create(
            name="Test service new",
            short_description="Test short desc new",
            png=SimpleUploadedFile(
                "test1.png",
                b"dummy png content",
                content_type="image/png",
            ),
            image=SimpleUploadedFile(
                "test1.jpg",
                b"dummy jpg content",
                content_type="image/jpeg",
            ),
            title="Test title new",
            content="Test content new",
            background_color="yellow",
        )

        cls.valid_data = {
            "meta_description": "This is a valid meta description within the required length range.",
            "meta_keywords": "keyword1, keyword2, keyword3, keyword4",
            "og_description": "This is a valid OG description for testing SEO constraints.",
        }

        cls.instance, created = ServiceDetailPageSeo.objects.get_or_create(
            service=cls.service
        )

        for key, value in cls.valid_data.items():
            setattr(cls.instance, key, value)
        cls.instance.save()

    def test_str_method(self):
        self.assert_str_method(
            self.instance,
            f"SEO ==> {self.service}",
        )

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_fields_min_length(self):
        self.assert_min_length(self.instance, "meta_description", 50)
        self.assert_min_length(self.instance, "meta_keywords", 50)
        self.assert_min_length(self.instance, "og_description", 50)

        with self.assertRaises(ValidationError) as cm:
            self.instance.full_clean()

        errors = cm.exception.message_dict
        self.assertIn("meta_description", errors)
        self.assertIn("meta_keywords", errors)
        self.assertIn("og_description", errors)

    def test_fields_max_length(self):
        self.assert_max_length(self.instance, "meta_description", 160)
        self.assert_max_length(self.instance, "meta_keywords", 160)
        self.assert_max_length(self.instance, "og_description", 160)

        with self.assertRaises(ValidationError) as cm:
            self.instance.full_clean()

        errors = cm.exception.message_dict
        self.assertIn("meta_description", errors)
        self.assertIn("meta_keywords", errors)
        self.assertIn("og_description", errors)

    def test_model(self):
        self.assert_model_instance(
            ServiceDetailPageSeo,
            "meta_description",
            self.valid_data["meta_description"],
        )
        self.assert_model_instance(
            ServiceDetailPageSeo,
            "meta_keywords",
            self.valid_data["meta_keywords"],
        )
        self.assert_model_instance(
            ServiceDetailPageSeo,
            "og_description",
            self.valid_data["og_description"],
        )
        self.assert_model_instance(
            ServiceDetailPageSeo,
            "service",
            self.service,
        )

    def test_automatically_created_service_detail_page_seo(
        self,
    ):
        service = Service.objects.create(
            name="Test",
            short_description="Test",
            png=SimpleUploadedFile(
                "test1.png",
                b"dummy png content",
                content_type="image/png",
            ),
            image=SimpleUploadedFile(
                "test1.jpg",
                b"dummy jpg content",
                content_type="image/jpeg",
            ),
            title="Test",
            content="Test",
            background_color="yellow",
        )

        deteail_page_seo_instance = ServiceDetailPageSeo.objects.get(
            service=service
        )

        self.assertEqual(
            deteail_page_seo_instance,
            service.detail_page_seo,
        )

    def test_unique_object_for_each_blog(self):
        service = Service.objects.first()

        with self.assertRaises(IntegrityError):
            ServiceDetailPageSeo.objects.create(service=service)
