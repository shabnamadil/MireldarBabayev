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
            "test1.png", 
            b"dummy png content", 
            content_type="image/png"
            ),
            image= SimpleUploadedFile(
            "test1.jpg", 
            b"dummy jpg content", 
            content_type="image/jpeg"
            ),
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

    def test_fields_max_length(self):
        self.assert_max_length(self.service, 'name', 200)
        self.assert_max_length(self.service, 'title', 60)
        self.assert_max_length(self.service, 'short_description', 160)
        self.assert_max_length(self.service, 'slug', 500)

    def test_fields_min_length(self):
        self.assert_min_length(self.service, 'title', 30)
        self.assert_min_length(self.service, 'short_description', 145)

    def test_object_count(self):
        self.assert_object_count(Service, 1)

    def test_deletion(self):
        self.assert_object_deleted(Service)

    def test_model(self):
        self.assert_model_instance(Service, 'name', 'Test service')
        self.assert_model_instance(Service, 'short_description', 'Test short desc')
        self.assert_model_instance(Service, 'title', 'Test title')
        self.assert_model_instance(Service, 'content', 'Test content')
        self.assert_model_instance(Service, 'background_color', 'blue')
        self.assertTrue(self.service.png.name.startswith('services/test1'))
        self.assertTrue(self.service.png.name.endswith('png'))
        self.assertTrue(self.service.image.name.startswith('services/images/test1'))
        self.assertTrue(self.service.image.name.endswith('jpg'))

    def test_slug_auto_generation(self):
        expected_slug = custom_slugify(self.service.title)
        self.assertEqual(self.service.slug, expected_slug)

    def test_get_absolute_url(self):
        expected_url = reverse('service-detail', args=[self.service.slug])
        self.assertEqual(self.service.get_absolute_url(), expected_url)