from django.urls import reverse_lazy

from apps.service.models import Service
from tests.utils.factories import ServiceFactory
from utils.tests.base import BaseValidationTest


class TestServiceListView(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse_lazy('services')
        cls.services = ServiceFactory.create_batch(6)

    def test_response_status_code(self):
        self.assert_status_code(self.url)

    def test_correct_template_used(self):
        self.assert_template_used(self.url, 'components/service/services.html')

    def test_all_services_in_context(self):
        self.assert_all_objects_in_context(self.url, 'services', self.services)

    def test_view_returns_all_services(self):
        self.assert_view_returns_all_objects(self.url, 'services', Service)

    def test_view_with_no_services(self):
        self.assert_view_without_context_data(Service, self.url, 'services')

    # other model data context need to be added after testing
