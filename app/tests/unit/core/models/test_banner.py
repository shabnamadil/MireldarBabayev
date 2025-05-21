from apps.core.models import Banner
from tests.utils.helpers import BaseValidationTest


class TestBannerModel(BaseValidationTest):

    def test_banner_str_returns_title(self):
        self.assert_str_output(Banner, "title", "Test banner")
