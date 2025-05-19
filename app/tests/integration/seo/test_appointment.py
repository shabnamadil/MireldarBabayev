from apps.seo.models import AppointmentPageSeo
from tests.utils.factories import AppointmentPageSeoFactory
from tests.utils.helpers import BasePageSeoTest, _ImageValidationTest
from utils.tests.base import BaseValidationTest


class TestAppointmentPageSeoModelIntegration(
    BaseValidationTest, _ImageValidationTest, BasePageSeoTest
):
    @classmethod
    def setUpTestData(cls):
        cls.object = AppointmentPageSeoFactory()
        cls.model = AppointmentPageSeo
        cls.image_field = 'og_image'
