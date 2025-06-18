from apps.seo.models import BlogsPageSeo
from tests.utils.helpers import BaseValidationTest


class TestBlogsPageSeoModel(BaseValidationTest):

    def test_blogs_page_seo_str_returns_meta_title(self):
        self.assert_str_output(BlogsPageSeo, "meta_title", "Meta title")
