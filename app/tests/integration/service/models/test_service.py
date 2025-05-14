from django.core.exceptions import ValidationError

from apps.service.models import Service
from tests.utils.factories import ServiceFactory
from utils.tests.base import BaseValidationTest


class TestServiceModelIntegration(BaseValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.service = ServiceFactory()

    def test_name_max_length(self):
        self.assert_max_length(self.service, 'name', 30)

    def test_short_description_max_length(self):
        self.assert_max_length(self.service, 'short_description', 160)

    def test_short_description_min_length(self):
        self.assert_min_length(self.service, 'short_description', 145)

    def test_title_max_length(self):
        self.assert_max_length(self.service, 'title', 60)

    def test_title_min_length(self):
        self.assert_min_length(self.service, 'title', 30)

    def test_content_max_length(self):
        self.assert_max_length(self.service, 'content', 1000)

    def test_content_min_length(self):
        self.assert_min_length(self.service, 'content', 300)

    def test_slug_max_length(self):
        self.assert_max_length(self.service, 'slug', 500)

    def test_title_unique(self):
        self.assert_unique_field(Service, 'title', 'Test title')

    def test_name_unique(self):
        self.assert_unique_field(Service, 'name', self.service.name)

    def test_name_required(self):
        self.assert_required_field(self.service, 'name')

    def test_short_description_required(self):
        self.assert_required_field(self.service, 'short_description')

    def test_png_required(self):
        self.assert_required_field(self.service, 'png')

    def test_image_required(self):
        self.assert_required_field(self.service, 'image')

    def test_title_required(self):
        self.assert_required_field(self.service, 'title')

    def test_content_required(self):
        self.assert_required_field(self.service, 'content')

    def test_background_color_required(self):
        self.assert_required_field(self.service, 'background_color')

    def test_raises_validation_error_when_invalid_background_color_choices(self):
        service = ServiceFactory.build(background_color='invalid_color')
        with self.assertRaises(ValidationError):
            service.full_clean()

    def test_object_count(self):
        self.assert_object_count(Service, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(Service)

    def test_service_name_saved_correctly(self):
        self.assert_model_instance(self.service, 'name', 'Test name')

    def test_service_short_description_saved_correctly(self):
        self.assert_model_instance(
            self.service, 'short_description', 'Test short description'
        )

    def test_service_png_saved_correctly(self):
        self.assertTrue(self.service.png.name.startswith('services/png/'))
        self.assertTrue(self.service.png.name.endswith('.png'))

    def test_service_image_saved_correctly(self):
        self.assertTrue(self.service.image.name.startswith('services/images/'))
        self.assertTrue(self.service.image.name.endswith('.jpg'))

    def test_service_title_saved_correctly(self):
        self.assert_model_instance(self.service, 'title', 'Test title')

    def test_service_content_saved_correctly(self):
        self.assert_model_instance(self.service, 'content', "Test content")

    def test_service_background_color_saved_correctly(self):
        self.assert_model_instance(self.service, 'background_color', 'blue')

    def test_slug_auto_generated(self):
        self.assert_slug_auto_generation(self.service, 'slug')

    # def test_raises_validation_error_when_incorrect_png_extension(self):
    #     service = ServiceFactory.build(png='test.txt')
    #     with self.assertRaises(ValidationError):
    #         service.full_clean()

    def test_object_is_instance_of_service(self):
        self.assertIsInstance(self.service, Service)

    # def test_png_file_upload(self):
    #     self.assert_file_upload(self.service, 'png', 'services/png/')

    # def test_image_file_upload(self):
    #     self.assert_file_upload(self.service, 'image', 'services/images/')
