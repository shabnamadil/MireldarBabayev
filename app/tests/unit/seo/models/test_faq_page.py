from apps.seo.models import FaqPageSeo
from utils.tests.base import BaseValidationTest


class TestFaqPageSeoModel(BaseValidationTest):

    def test_faq_page_seo_str_returns_meta_title(self):
        self.assert_str_output(FaqPageSeo, 'meta_title', 'Meta title')
