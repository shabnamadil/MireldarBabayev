from apps.seo.models import AboutUsPageSeo
from tests.utils.helpers import BaseValidationTest


class TestAboutUsPageSeoModel(BaseValidationTest):

    def test_about_us_page_seo_str_returns_meta_title(self):
        self.assert_str_output(AboutUsPageSeo, "meta_title", "Meta title")
