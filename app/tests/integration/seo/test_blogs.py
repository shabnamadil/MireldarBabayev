from apps.seo.models import BlogsPageSeo
from tests.utils.factories import BlogsPageSeoFactory
from tests.utils.helpers import BasePageSeoTest, _ImageValidationTest
from utils.tests.base import BaseValidationTest


class TestBlogsPageSeoModelIntegration(
    BaseValidationTest, _ImageValidationTest, BasePageSeoTest
):
    @classmethod
    def setUpTestData(cls):
        cls.object = BlogsPageSeoFactory()
        cls.model = BlogsPageSeo
        cls.image_field = 'og_image'
