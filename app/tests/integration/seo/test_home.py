from apps.seo.models import HomePageSeo
from tests.utils.factories import HomePageSeoFactory
from tests.utils.helpers import (
    BaseSeoPageTest,
    BaseValidationTest,
    _ImageValidationTest,
)


class TestHomePageSeoModelIntegration(
    BaseValidationTest, _ImageValidationTest, BaseSeoPageTest
):
    @classmethod
    def setUpTestData(cls):
        cls.object = HomePageSeoFactory()
        cls.model = HomePageSeo
        cls.image_field = "og_image"
