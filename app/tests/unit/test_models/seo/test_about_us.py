from django.core.exceptions import ValidationError

from apps.seo.models import AboutUsPageSeo
from utils.tests.seo import BaseSeoTest


class TestAboutUsPageSeoModel(BaseSeoTest):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.instance = AboutUsPageSeo.objects.create(**cls.valid_data)
        cls.model = AboutUsPageSeo

    def test_str_method(self):
        self.assert_str_method(self.instance, self.valid_data["meta_title"])

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_singleton(self):
        self.assert_singleton(self.model)

    def test_image_field(self):
        self.assertTrue(
            self.instance.og_image.name.startswith("seo-images/about-us/")
        )

    def test_fields_min_length(self):
        self.assert_min_length(self.instance, "meta_title", 30)
        self.assert_min_length(self.instance, "meta_description", 50)
        self.assert_min_length(self.instance, "meta_keywords", 50)
        self.assert_min_length(self.instance, "og_title", 30)
        self.assert_min_length(self.instance, "og_description", 50)

        with self.assertRaises(ValidationError) as cm:
            self.instance.full_clean()

        errors = cm.exception.message_dict
        self.assertIn("meta_title", errors)
        self.assertIn("meta_description", errors)
        self.assertIn("meta_keywords", errors)
        self.assertIn("og_title", errors)
        self.assertIn("og_description", errors)

    def test_fields_max_length(self):
        self.assert_max_length(self.instance, "meta_title", 60)
        self.assert_max_length(self.instance, "meta_description", 160)
        self.assert_max_length(self.instance, "meta_keywords", 160)
        self.assert_max_length(self.instance, "og_title", 60)
        self.assert_max_length(self.instance, "og_description", 160)

        with self.assertRaises(ValidationError) as cm:
            self.instance.full_clean()

        errors = cm.exception.message_dict
        self.assertIn("meta_title", errors)
        self.assertIn("meta_description", errors)
        self.assertIn("meta_keywords", errors)
        self.assertIn("og_title", errors)
        self.assertIn("og_description", errors)

    def test_model(self):
        self.assert_model_instance(
            AboutUsPageSeo, 'meta_title', self.valid_data["meta_title"]
        )
        self.assert_model_instance(
            AboutUsPageSeo,
            'meta_description',
            self.valid_data["meta_description"],
        )
        self.assert_model_instance(
            AboutUsPageSeo, 'meta_keywords', self.valid_data["meta_keywords"]
        )
        self.assert_model_instance(
            AboutUsPageSeo, 'og_title', self.valid_data["og_title"]
        )
        self.assert_model_instance(
            AboutUsPageSeo, 'og_description', self.valid_data["og_description"]
        )
        self.assertTrue(
            self.instance.og_image.name.startswith('seo-images/about-us/')
        )
        self.assertTrue(self.instance.og_image.name.endswith('jpg'))
