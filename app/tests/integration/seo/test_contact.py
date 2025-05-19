from apps.seo.models import ContactPageSeo
from tests.utils.factories import ContactPageSeoFactory
from tests.utils.helpers import BasePageSeoTest, _ImageValidationTest
from utils.tests.base import BaseValidationTest


class TestContactPageSeoModelIntegration(
    BaseValidationTest, _ImageValidationTest, BasePageSeoTest
):
    @classmethod
    def setUpTestData(cls):
        cls.object = ContactPageSeoFactory()
        cls.model = ContactPageSeo
        cls.image_field = 'og_image'
