from apps.seo.models import ServicesPageSeo
from tests.utils.factories import ServicesPageSeoFactory
from tests.utils.helpers import (
    BaseSeoPageTest,
    BaseValidationTest,
    _ImageValidationTest,
)


class TestServicesPageSeoModelIntegration(
    BaseValidationTest, _ImageValidationTest, BaseSeoPageTest
):
    @classmethod
    def setUpTestData(cls):
        cls.object = ServicesPageSeoFactory()
        cls.model = ServicesPageSeo
        cls.image_field = "og_image"
