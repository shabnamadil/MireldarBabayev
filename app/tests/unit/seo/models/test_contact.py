from apps.seo.models import ContactPageSeo
from tests.utils.helpers import BaseValidationTest


class TestContactPageSeoModel(BaseValidationTest):

    def test_contact_page_seo_str_returns_meta_title(self):
        self.assert_str_output(ContactPageSeo, "meta_title", "Meta title")
