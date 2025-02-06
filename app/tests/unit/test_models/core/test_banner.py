from django.core.exceptions import ValidationError

from apps.core.models import Banner
from utils.tests.base import BaseValidationTest


class TestBannerModel(BaseValidationTest):
    
    @classmethod
    def setUpTestData(cls):
        cls.banner = Banner.objects.create(
            title='Banner title',
            subtitle='Banner subtitle',
            description='Banner description',
            png='banner/1.png',
            video_id='MKG_6BqnhpI'
        )

    def test_banner_model(self):
        self.assert_model_instance(Banner, 'title', 'Banner title')
        self.assert_model_instance(Banner, 'subtitle', 'Banner subtitle')
        self.assert_model_instance(Banner, 'description', 'Banner description')
        self.assert_model_instance(Banner, 'png', 'banner/1.png')
        self.assert_model_instance(Banner, 'video_id', 'MKG_6BqnhpI')

    def test_str_method(self):
        self.assert_str_method(self.banner, 'Banner title')

    def test_title_unique(self):
        self.assert_unique_field(Banner, 'title', 'Banner title')

    def test_subtitle_unique(self):
        self.assert_unique_field(Banner, 'subtitle', 'Banner subtitle')

    def test_description_unique(self):
        self.assert_unique_field(Banner, 'description', 'Banner description')

    def test_video_id_unique(self):
        self.assert_unique_field(Banner, 'video_id', 'MKG_6BqnhpI')

    def test_video_id_max_length(self):
        self.assert_max_length(self.banner, 'video_id', 11)

    def test_title_max_length(self):
        self.assert_max_length(self.banner, 'title', 100)

    def test_subtitle_max_length(self):
        self.assert_max_length(self.banner, 'subtitle', 100)

    def test_png_file_extension(self):
        self.banner.png.name = 'banner/1.jpg'
        with self.assertRaises(ValidationError):
            self.banner.full_clean()

    def test_object_count(self):
        self.assert_object_count(Banner, 1)

    def test_deletion(self):
        self.assert_object_deleted(Banner)