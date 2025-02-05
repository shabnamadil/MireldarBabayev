from django.core.exceptions import ValidationError

from apps.core.models import SiteSettings
from utils.tests.base import BaseValidationTest


class TestSiteSettingsModel(BaseValidationTest):
    
    @classmethod
    def setUpTestData(cls):
        cls.site_settings = SiteSettings.objects.create(
            site_name='a' * 30,
            logo='logos/test.png',
            favicon='favicons/test.png',
            location='Test location',
            number='+1234567890',
            email='test@gmail.com',
            work_hours='09:00 - 18:00',
            map_url='src',
            facebook='https://facebook.com',
            youtube='https://youtube.com',
            instagram='https://instagram.com',
            twitter='https://twitter.com',
            linkedin='https://linkedin.com',
            tiktok='https://tiktok.com',
            footer_description='Test footer description'
        )

    def test_model(self):
        self.assert_model_instance(SiteSettings, 'site_name', 'a' * 30)
        self.assert_model_instance(SiteSettings, 'logo', 'logos/test.png')
        self.assert_model_instance(SiteSettings, 'favicon', 'favicons/test.png')
        self.assert_model_instance(SiteSettings, 'location', 'Test location')
        self.assert_model_instance(SiteSettings, 'number', '+1234567890')
        self.assert_model_instance(SiteSettings, 'email', 'test@gmail.com')
        self.assert_model_instance(SiteSettings, 'work_hours', '09:00 - 18:00')
        self.assert_model_instance(SiteSettings, 'map_url', 'src')
        self.assert_model_instance(SiteSettings, 'facebook', 'https://facebook.com')
        self.assert_model_instance(SiteSettings, 'youtube', 'https://youtube.com')
        self.assert_model_instance(SiteSettings, 'instagram', 'https://instagram.com')
        self.assert_model_instance(SiteSettings, 'twitter', 'https://twitter.com')
        self.assert_model_instance(SiteSettings, 'linkedin', 'https://linkedin.com')
        self.assert_model_instance(SiteSettings, 'tiktok', 'https://tiktok.com')
        self.assert_model_instance(SiteSettings, 'footer_description', 'Test footer description')

    def str_method(self):
        self.assert_str_method(self.site_settings, 'Test')

    def test_singleton_model(self):
        self.assert_singleton(SiteSettings)

    def test_object_count(self):
        self.assert_object_count(SiteSettings, 1)

    def test_site_name_min_length(self):
        self.assert_min_length(self.site_settings, 'site_name', 30)

    def test_site_name_max_length(self):
        self.assert_max_length(self.site_settings, 'site_name', 100)

    def test_location_max_length(self):
        self.assert_max_length(self.site_settings, 'location', 100)

    def test_work_hours_max_length(self):
        self.assert_max_length(self.site_settings, 'work_hours', 13)

    def test_map_url_max_length(self): 
        self.assert_max_length(self.site_settings, 'map_url', 500)

    def test_number_max_length(self):
        self.assert_max_length(self.site_settings, 'number', 17)

    def test_number(self):
        self.assert_invalid_number(self.site_settings, number_field='number')

    def test_email(self):
        self.assert_invalid_email(self.site_settings, email_field='email')

    def test_work_hours(self):
        invalid_work_hours = [
            '9:00 - 18:00',   # Missing leading zero
            '09:00-18:00',    # Missing space
            '09:00 -18:00',   # Missing space
            '25:00 - 18:00',  # Invalid hour
            '09:00 - 60:00',  # Invalid minute
            '09:00 / 18:00',   # Wrong separator
            '22:00 - 18:00',  # Start time is after end time
            '09:00 - 09:00',   # Start time is equal to end time,
            '18:00 - 09:00',   # Start time is after end time
            '59:68 - 09:00',   # Invalid start 
            '09:00 - 59:68',   # Invalid end
        ]

        for work_hour in invalid_work_hours:
            self.site_settings.work_hours = work_hour
            with self.assertRaises(ValidationError):
                self.site_settings.full_clean()