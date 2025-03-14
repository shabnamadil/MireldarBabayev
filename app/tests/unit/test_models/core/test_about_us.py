from django.core.files.uploadedfile import SimpleUploadedFile

from apps.core.models import AboutUs
from utils.tests.base import BaseValidationTest


class TestAboutUsModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.about_us = AboutUs.objects.create(
            video_id='MKG_6BqnhpI',
            mission='Missiyamız',
            vision='Görüşümüz',
            value='Dəyərlərimiz',
            content='Haqqımızda səhifəsi üçün kontent',
            image=SimpleUploadedFile(
                "test1.jpg", b"dummy jpg content", content_type="image/jpeg"
            ),
        )

    def test_about_us_model(self):
        self.assert_model_instance(AboutUs, 'video_id', 'MKG_6BqnhpI')
        self.assert_model_instance(AboutUs, 'mission', 'Missiyamız')
        self.assert_model_instance(AboutUs, 'vision', 'Görüşümüz')
        self.assert_model_instance(AboutUs, 'value', 'Dəyərlərimiz')
        self.assert_model_instance(
            AboutUs, 'content', 'Haqqımızda səhifəsi üçün kontent'
        )
        self.assertTrue(self.about_us.image.name.startswith('about/'))
        self.assertTrue(self.about_us.image.name.endswith('jpg'))

    def test_str_method(self):
        self.assert_str_method(self.about_us, 'Haqqımızda məlumat')

    def test_singleton_model(self):
        self.assert_singleton(AboutUs)

    def test_object_count(self):
        self.assert_object_count(AboutUs, 1)

    def test_deletion(self):
        self.assert_object_deleted(AboutUs)

    def test_video_id_length(self):
        self.assert_max_length(self.about_us, 'video_id', 11)
