from django.core.exceptions import ValidationError
from django.db import IntegrityError

from apps.seo.models import ServiceDetailPageSeo
from apps.service.models import Service
from tests.utils.factories import ServiceFactory
from tests.utils.helpers import _ImageValidationTest, _PngValidationTest
from utils.tests.base import BaseValidationTest


class TestServiceModelIntegration(
    BaseValidationTest, _PngValidationTest, _ImageValidationTest
):
    @classmethod
    def setUpTestData(cls):
        cls.factory = ServiceFactory
        cls.object = cls.factory()
        cls.model = Service
        cls.image_field = 'image'

    def test_name_max_length(self):
        self.assert_max_length(self.object, 'name', 30)

    def test_short_description_max_length(self):
        self.assert_max_length(self.object, 'short_description', 160)

    def test_short_description_min_length(self):
        self.assert_min_length(self.object, 'short_description', 145)

    def test_title_max_length(self):
        self.assert_max_length(self.object, 'title', 60)

    def test_title_min_length(self):
        self.assert_min_length(self.object, 'title', 30)

    def test_content_max_length(self):
        self.assert_max_length(self.object, 'content', 1000)

    def test_content_min_length(self):
        self.assert_min_length(self.object, 'content', 300)

    def test_slug_max_length(self):
        self.assert_max_length(self.object, 'slug', 500)

    def test_title_unique(self):
        self.assert_unique_field(self.model, 'title', self.object.title)

    def test_name_unique(self):
        self.assert_unique_field(self.model, 'name', self.object.name)

    def test_name_required(self):
        self.assert_required_field(self.object, 'name')

    def test_short_description_required(self):
        self.assert_required_field(self.object, 'short_description')

    def test_png_required(self):
        self.assert_required_field(self.object, 'png')

    def test_image_required(self):
        self.assert_required_field(self.object, 'image')

    def test_title_required(self):
        self.assert_required_field(self.object, 'title')

    def test_content_required(self):
        self.assert_required_field(self.object, 'content')

    def test_background_color_required(self):
        self.assert_required_field(self.object, 'background_color')

    def test_raises_validation_error_when_invalid_background_color_choices(self):
        service = self.factory.build(background_color='invalid_color')
        with self.assertRaises(ValidationError):
            service.full_clean()

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_service_name_saved_correctly(self):
        self.assert_model_instance(self.object, 'name', self.object.name)

    def test_service_short_description_saved_correctly(self):
        self.assert_model_instance(
            self.object, 'short_description', self.object.short_description
        )

    def test_service_png_saved_correctly(self):
        self.assertTrue(self.object.png.name.startswith('services/png/'))
        self.assertTrue(self.object.png.name.endswith('.png'))

    def test_service_image_saved_correctly(self):
        self.assertTrue(self.object.image.name.startswith('services/images/'))
        self.assertTrue(self.object.image.name.endswith('.jpg'))

    def test_service_title_saved_correctly(self):
        self.assert_model_instance(self.object, 'title', self.object.title)

    def test_service_content_saved_correctly(self):
        self.assert_model_instance(self.object, 'content', self.object.content)

    def test_service_background_color_saved_correctly(self):
        self.assert_model_instance(
            self.object, 'background_color', self.object.background_color
        )

    def test_slug_auto_generated(self):
        self.assert_slug_auto_generation(self.object, 'slug')

    def test_object_is_instance_of_service(self):
        self.assertIsInstance(self.object, self.model)

    def test_services_are_ordered_by_created_at_desc(self):
        self.assert_ordering(self.factory, self.model)

    def test_creating_service_also_creates_related_seo_instance(self):
        seo_instance = ServiceDetailPageSeo.objects.filter(service=self.object)
        self.assertTrue(seo_instance.exists())

    def test_creating_second_service_detail_page_seo_raises_integrity_error(self):
        with self.assertRaises(IntegrityError):
            ServiceDetailPageSeo.objects.create(service=self.object)

    def test_deleting_service_also_deletes_related_seo_instance(self):
        deleted_service_object = self.object.delete()
        seo_instance = ServiceDetailPageSeo.objects.filter(
            service=deleted_service_object
        ).first()
        self.assertIsNone(seo_instance)
