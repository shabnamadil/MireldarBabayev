from apps.seo.models import FaqPageSeo
from tests.utils.factories import FaqPageSeoFactory
from tests.utils.helpers import (
    BaseSeoPageTest,
    BaseValidationTest,
    _ImageValidationTest,
)


class TestFaqPageSeoModelIntegration(
    BaseValidationTest, _ImageValidationTest, BaseSeoPageTest
):
    @classmethod
    def setUpTestData(cls):
        cls.object = FaqPageSeoFactory()
        cls.model = FaqPageSeo
        cls.image_field = "og_image"
