from apps.seo.models import HomePageSeo
from utils.tests.base import BaseValidationTest


class TestHomePageSeoModel(BaseValidationTest):

    def test_home_page_seo_str_returns_meta_title(self):
        self.assert_str_output(HomePageSeo, "meta_title", "Meta title")
