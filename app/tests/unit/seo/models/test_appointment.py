from apps.seo.models import AppointmentPageSeo
from utils.tests.base import BaseValidationTest


class TestAppointmentPageSeoModel(BaseValidationTest):

    def test_appointment_page_seo_str_returns_meta_title(self):
        self.assert_str_output(AppointmentPageSeo, "meta_title", "Meta title")
