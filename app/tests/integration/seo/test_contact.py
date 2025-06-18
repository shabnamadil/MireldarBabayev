from apps.seo.models import ContactPageSeo
from tests.utils.factories import ContactPageSeoFactory
from tests.utils.helpers import (
    BaseSeoPageTest,
    BaseValidationTest,
    _ImageValidationTest,
)


class TestContactPageSeoModelIntegration(
    BaseValidationTest, _ImageValidationTest, BaseSeoPageTest
):
    @classmethod
    def setUpTestData(cls):
        cls.object = ContactPageSeoFactory()
        cls.model = ContactPageSeo
        cls.image_field = "og_image"
