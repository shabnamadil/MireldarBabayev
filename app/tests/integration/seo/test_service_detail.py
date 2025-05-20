from django.db import IntegrityError

from apps.seo.models import ServiceDetailPageSeo
from tests.utils.factories import ServiceDetailPageSeoFactory, ServiceFactory
from tests.utils.helpers import BaseSeoDetailPageTest, BaseValidationTest


class TestServiceDetailPageSeoModelIntegration(
    BaseValidationTest, BaseSeoDetailPageTest
):
    @classmethod
    def setUpTestData(cls):
        cls.service = ServiceFactory()
        cls.object = cls.service.detail_page_seo
        cls.model = ServiceDetailPageSeo

    def test_raises_integrity_error_without_service_creation(self):
        with self.assertRaises(IntegrityError):
            ServiceDetailPageSeoFactory(service=None)
