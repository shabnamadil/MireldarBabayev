from django.core.exceptions import ValidationError

from utils.tests.base import BaseValidationTest
from apps.service.models import WhyChooseUs


class TestWhyChooseUsModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.object = WhyChooseUs.objects.create(
            title='Test object',
            short_description='Test desc',
            png='test/1.png'
        )

    def test_str_method(self):
        self.assert_str_method(self.object, 'Test object')

    def test_unique_title(self):
        self.assert_unique_field(WhyChooseUs, 'title', 'Test object')

    def test_title_max_length(self):
        self.assert_max_length(self.object, 'title', 200)

    def test_model(self):
        self.assert_model_instance(WhyChooseUs, 'title', 'Test object')
        self.assert_model_instance(WhyChooseUs, 'short_description', 'Test desc')
        self.assert_model_instance(WhyChooseUs, 'png', 'test/1.png')

    def test_object_count(self):
        self.assert_object_count(WhyChooseUs, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(WhyChooseUs)

    def test_png_extension(self):
        self.object.png = 'test/1.jpg'
        with self.assertRaises(ValidationError):
            self.object.full_clean()