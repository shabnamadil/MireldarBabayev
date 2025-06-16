from apps.seo.models import AboutUsPageSeo
from tests.utils.factories import AboutUsPageSeoFactory
from tests.utils.helpers import (
    BaseSeoPageTest,
    BaseValidationTest,
    _ImageValidationTest,
)


class TestAboutUsPageSeoModelIntegration(
    BaseValidationTest, _ImageValidationTest, BaseSeoPageTest
):
    @classmethod
    def setUpTestData(cls):
        cls.object = AboutUsPageSeoFactory()
        cls.model = AboutUsPageSeo
        cls.image_field = "og_image"
