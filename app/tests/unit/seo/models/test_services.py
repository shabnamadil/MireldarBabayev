from apps.seo.models import ServicesPageSeo
from tests.utils.helpers import BaseValidationTest


class TestServicesPageSeoModel(BaseValidationTest):

    def test_services_page_seo_str_returns_meta_title(self):
        self.assert_str_output(ServicesPageSeo, "meta_title", "Meta title")
