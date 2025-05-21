from apps.core.models import SiteSettings
from tests.utils.helpers import BaseValidationTest


class TestSiteSettingsModel(BaseValidationTest):

    def test_site_settings_str_returns_question(self):
        self.assert_str_output(SiteSettings, "site_name", "Test site name")
