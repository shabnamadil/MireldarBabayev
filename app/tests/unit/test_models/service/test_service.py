from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from apps.service.models import Service
from utils.tests.base import BaseValidationTest
from utils.helpers.slugify import custom_slugify


class TestServiceModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.service = Service.objects.create(
            name='Test service',
            short_description='Test short desc',
            png= SimpleUploadedFile(
            "test.png", b"dummy png content", content_type="test/1.png"
        ),
            image='test/1.jpg',
            title='Test title',
            content='Test content',
            background_color='blue'
        )

    def test_str_method(self):
        self.assert_str_method(self.service, 'Test service')

    def test_name_unique(self):
        self.assert_unique_field(Service, 'name', 'Test service')

    def test_title_unique(self):
        self.assert_unique_field(Service, 'title', 'Test title')

    def test_name_max_length(self):
        self.assert_max_length(self.service, 'name', 200)

    def test_title_max_length(self):
        self.assert_max_length(self.service, 'title', 60)

    def test_title_min_length(self):
        self.assert_min_length(self.service, 'title', 30)

    def test_short_desc_max_length(self):
        self.assert_max_length(self.service, 'short_description', 160)

    def test_short_desc_min_length(self):
        self.assert_min_length(self.service, 'short_description', 145)

    def test_object_count(self):
        self.assert_object_count(Service, 1)

    def test_deletion(self):
        self.assert_object_deleted(Service)

    def test_model(self):
        self.assert_model_instance(Service, 'name', 'Test service')
        self.assert_model_instance(Service, 'short_description', 'Test short desc')
        self.assert_model_instance(Service, 'png', 'test/1.png')
        self.assert_model_instance(Service, 'image', 'test/1.jpg')
        self.assert_model_instance(Service, 'title', 'Test title')
        self.assert_model_instance(Service, 'content', 'Test content')
        self.assert_model_instance(Service, 'background_color', 'blue')

    def test_slug_auto_generation(self):
        """Test that the slug is auto-generated from the title using custom_slugify."""
        expected_slug = custom_slugify(self.service.title)
        self.assertEqual(self.service.slug, expected_slug)

    def test_get_absolute_url(self):
        """Test that get_absolute_url returns the proper URL."""
        expected_url = reverse('service-detail', args=[self.service.slug])
        self.assertEqual(self.service.get_absolute_url(), expected_url)

    def test_slug_max_length(self):
        self.assert_max_length(self.service, 'slug', 500)

        