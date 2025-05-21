from apps.core.models import SiteSettings
from tests.utils.factories import SiteSettingsFactory
from tests.utils.helpers import (
    BaseValidationTest,
    _MapUrlValidationTest,
    _PngValidationTest,
    _WorkHourValidationTest,
)


class TestSiteSettingsLogoValidation(
        BaseValidationTest,
        _PngValidationTest,
        _MapUrlValidationTest,
        _WorkHourValidationTest
):
    @classmethod
    def setUpTestData(cls):
        cls.factory = SiteSettingsFactory
        cls.object = cls.factory()
        cls.model = SiteSettings
        cls.png_field = 'logo'

    def test_logo_required(self):
        self.assert_required_field(self.object, "logo")

    def test_logo_saved_correctly(self):
        self.assertTrue(self.object.logo.name.startswith("logos/"))
        self.assertTrue(self.object.logo.name.endswith(".png"))


class TestSiteSettingsFaviconValidation(BaseValidationTest, _PngValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = SiteSettingsFactory
        cls.object = cls.factory()
        cls.model = SiteSettings
        cls.png_field = 'favicon'

    def test_favicon_required(self):
        self.assert_required_field(self.object, "favicon")

    def test_favicon_saved_correctly(self):
        self.assertTrue(self.object.favicon.name.startswith("favicons/"))
        self.assertTrue(self.object.favicon.name.endswith(".png"))


class TestSiteSettingsModelIntegration(BaseValidationTest, _WorkHourValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = SiteSettingsFactory
        cls.object = cls.factory()
        cls.model = SiteSettings
        cls.work_hour_field = 'work_hours'

    def test_site_name_max_length(self):
        self.assert_max_length(self.object, "site_name", 100)

    def test_site_name_min_length(self):
        self.assert_min_length(self.object, "site_name", 30)

    def test_location_max_length(self):
        self.assert_max_length(self.object, "location", 100)

    def test_number_max_length(self):
        self.assert_max_length(self.object, "number", 17)

    def test_work_hours_max_length(self):
        self.assert_max_length(self.object, "work_hours", 13)

    def test_map_url_max_length(self):
        self.assert_max_length(self.object, "map_url", 500)

    def test_footer_description_max_length(self):
        self.assert_max_length(self.object, "footer_description", 200)

    def test_site_name_required(self):
        self.assert_required_field(self.object, "site_name")

    def test_location_required(self):
        self.assert_required_field(self.object, "location")

    def test_number_required(self):
        self.assert_required_field(self.object, "number")

    def test_email_required(self):
        self.assert_required_field(self.object, "email")

    def test_work_hours_required(self):
        self.assert_required_field(self.object, "work_hours")

    def test_map_url_required(self):
        self.assert_required_field(self.object, "map_url")

    def test_footer_description_required(self):
        self.assert_required_field(self.object, "footer_description")

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_singleton(self):
        self.assert_singleton(self.model)

    def test_site_name_saved_correctly(self):
        self.assert_model_instance(self.object, "site_name", self.object.site_name)

    def test_location_saved_correctly(self):
        self.assert_model_instance(self.object, "location", self.object.location)

    def test_number_saved_correctly(self):
        self.assert_model_instance(self.object, "number", self.object.number)

    def test_email_saved_correctly(self):
        self.assert_model_instance(self.object, "email", self.object.email)

    def test_work_hours_saved_correctly(self):
        self.assert_model_instance(self.object, "work_hours", self.object.work_hours)

    def test_map_url_saved_correctly(self):
        self.assert_model_instance(self.object, "map_url", self.object.map_url)

    def test_facebook_saved_correctly(self):
        self.assert_model_instance(self.object, "facebook", self.object.facebook)

    def test_youtube_saved_correctly(self):
        self.assert_model_instance(self.object, "youtube", self.object.youtube)

    def test_twitter_saved_correctly(self):
        self.assert_model_instance(self.object, "twitter", self.object.twitter)

    def test_instagram_saved_correctly(self):
        self.assert_model_instance(self.object, "instagram", self.object.instagram)

    def test_linkedin_saved_correctly(self):
        self.assert_model_instance(self.object, "linkedin", self.object.linkedin)

    def test_tiktok_saved_correctly(self):
        self.assert_model_instance(self.object, "tiktok", self.object.tiktok)

    def test_footer_description_saved_correctly(self):
        self.assert_model_instance(
            self.object,
            "footer_description",
            self.object.footer_description)

    def test_object_is_instance_of_site_settings(self):
        self.assertIsInstance(self.object, self.model)

    def test_invalid_email_raises_validation_error(self):
        self.assert_invalid_email(self.object)

    def test_invalid_phone_number_raises_validation_error(self):
        self.assert_invalid_number(self.object, "number")

    def test_valid_facebook_url(self):
        self.assert_valid_social_media_urls(
            self.object, 'facebook', 'https://facebook.com/')

    def test_invalid_facebook_url(self):
        self.assert_invalid_social_media_urls(self.object, 'facebook')

    def test_valid_instagram_url(self):
        self.assert_valid_social_media_urls(
            self.object, 'instagram', 'https://instagram.com/')

    def test_invalid_instagram_url(self):
        self.assert_invalid_social_media_urls(self.object, 'instagram')

    def test_valid_twitter_url(self):
        self.assert_valid_social_media_urls(
            self.object, 'twitter', 'https://twitter.com/')

    def test_invalid_twitter_url(self):
        self.assert_invalid_social_media_urls(self.object, 'twitter')

    def test_valid_linkedin_url(self):
        self.assert_valid_social_media_urls(
            self.object, 'linkedin', 'https://linkedin.com/')

    def test_invalid_linkedin_url(self):
        self.assert_invalid_social_media_urls(self.object, 'linkedin')

    def test_valid_youtube_url(self):
        self.assert_valid_social_media_urls(
            self.object, 'youtube', 'https://youtube.com/')

    def test_invalid_youtube_url(self):
        self.assert_invalid_social_media_urls(self.object, 'youtube')

    def test_valid_tiktok_url(self):
        self.assert_valid_social_media_urls(
            self.object, 'tiktok', 'https://tiktok.com/')

    def test_invalid_tiktok_url(self):
        self.assert_invalid_social_media_urls(self.object, 'tiktok')

    def test_facebook_field_type(self):
        self.assert_field_type(self.object, 'facebook', 'a')

    def test_instagram_field_type(self):
        self.assert_field_type(self.object, 'instagram', 'a')

    def test_youtube_field_type(self):
        self.assert_field_type(self.object, 'youtube', 'a')

    def test_twitter_field_type(self):
        self.assert_field_type(self.object, 'twitter', 'a')

    def test_linkedin_field_type(self):
        self.assert_field_type(self.object, 'linkedin', 'a')

    def test_tiktok_field_type(self):
        self.assert_field_type(self.object, 'tiktok', 'a')
