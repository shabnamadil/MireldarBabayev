from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from apps.core.models import Banner


class TestBannerModel(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.banner = Banner.objects.create(
            title='Banner title',
            subtitle='Banner subtitle',
            description='Banner description',
            png='banner/1.png',
            video_id='MKG_6BqnhpI'
        )

    def test_str_method(self):
        self.assertEqual(str(self.banner), "Banner title")

    def test_title_unique(self):
        with self.assertRaises(IntegrityError):
            Banner.objects.create(
                title='Banner title',
            )

    def test_subtitle_unique(self):
        with self.assertRaises(IntegrityError):
            Banner.objects.create(
                subtitle='Banner subtitle',
            )

    def test_description_unique(self):
        with self.assertRaises(IntegrityError):
            Banner.objects.create(
                description='Banner description',
            )

    def test_video_id_unique(self):
        with self.assertRaises(IntegrityError):
            Banner.objects.create(
                video_id='MKG_6BqnhpI',
            )

    def test_second_object_creation(self):
        try:
            Banner.objects.create(
            title='Banner second title',
            subtitle='Banner second subtitle',
            description='Banner second description',
            png='banner/1.png',
            video_id='MKG_6Bqnhp2'
        )
        except IntegrityError:
            self.fail("IntegrityError was raised unexpectedly!")

    def test_video_id_length(self):
        self.banner.video_id = 'MKG_6BqnhpI123'
        with self.assertRaises(ValidationError):
            self.banner.full_clean()

    def test_png_file_extension(self):
        self.banner.png.name = 'banner/1.jpg'
        with self.assertRaises(ValidationError):
            self.banner.full_clean()