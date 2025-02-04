from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from apps.core.models import AboutUs


class TestAboutUsModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.about_us = AboutUs.objects.create(
            video_id='MKG_6BqnhpI',
            mission='Missiyamız',
            vision='Görüşümüz',
            value='Dəyərlərimiz',
            content='Haqqımızda səhifəsi üçün kontent',
            image='about/1.jpg'
        )

    def test_str_method(self):
        self.assertEqual(str(self.about_us), "Haqqımızda məlumat")

    def test_singleton_model(self):
        with self.assertRaises(IntegrityError):
            AboutUs.objects.create()

    def test_object_count(self):
        self.assertEqual(AboutUs.objects.count(), 1)

    def test_verbose_name(self):
        self.assertEqual(AboutUs._meta.verbose_name, "Haqqımızda")

    def test_deletion(self):
        self.about_us.delete()
        new_about_us = AboutUs.objects.create()
        self.assertEqual(AboutUs.objects.count(), 1)

    def test_video_id_length(self):
        self.about_us.video_id = 'MKG_6BqnhpI123'
        with self.assertRaises(ValidationError):
            self.about_us.full_clean()
