from apps.seo.models import AppointmentPageSeo
from tests.utils.factories import AppointmentPageSeoFactory
from tests.utils.helpers import (
    BaseSeoPageTest,
    BaseValidationTest,
    _ImageValidationTest,
)


class TestAppointmentPageSeoModelIntegration(
    BaseValidationTest, _ImageValidationTest, BaseSeoPageTest
):
    @classmethod
    def setUpTestData(cls):
        cls.object = AppointmentPageSeoFactory()
        cls.model = AppointmentPageSeo
        cls.image_field = "og_image"
