from django.core.files.uploadedfile import SimpleUploadedFile

from apps.core.models import Testimoinal
from utils.tests.base import BaseValidationTest


class TestimoinalModelTest(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.testimonial = Testimoinal.objects.create(
            client_image=SimpleUploadedFile(
                "test1.jpg", b"dummy jpg content", content_type="image/jpeg"
            ),
            client_full_name='Test Test',
            client_profession='Test profession',
            client_comment='Test comment',
            star=5,
        )

    def test_testimonial_model(self):
        self.assert_model_instance(
            Testimoinal, 'client_full_name', 'Test Test'
        )
        self.assert_model_instance(
            Testimoinal, 'client_profession', 'Test profession'
        )
        self.assert_model_instance(
            Testimoinal, 'client_comment', 'Test comment'
        )
        self.assert_model_instance(Testimoinal, 'star', 5)
        self.assert_model_instance(Testimoinal, 'star_range', range(5))
        self.assertTrue(
            self.testimonial.client_image.name.startswith('testimonials/')
        )
        self.assertTrue(self.testimonial.client_image.name.endswith('jpg'))

    def test_str_method(self):
        self.assert_str_method(self.testimonial, 'Test Test-in rəyi')

    def test_fields_max_length(self):
        self.assert_max_length(self.testimonial, 'client_full_name', 20)
        self.assert_max_length(self.testimonial, 'client_profession', 100)
        self.assert_max_length(self.testimonial, 'client_comment', 155)
        self.assert_max_length(self.testimonial, 'star', 5)

    def test_fields_min_length(self):
        self.assert_min_length(self.testimonial, 'client_comment', 150)
        self.assert_min_length(self.testimonial, 'star', 1)

    def test_star_type(self):
        self.assert_field_type(self.testimonial, 'star', 'a')

    def test_object_count(self):
        self.assertEqual(Testimoinal.objects.count(), 1)

    def test_deletion(self):
        self.assert_object_deleted(Testimoinal)
