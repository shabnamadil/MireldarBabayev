from django.urls import reverse_lazy

from apps.service.models import Download, Service
from tests.utils.factories import DownloadFactory, ServiceFactory
from utils.tests.base import BaseValidationTest


class TestServiceDetailView(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.other_services = ServiceFactory.create_batch(3)
        cls.main_service = cls.other_services[0]
        cls.url = reverse_lazy('service-detail', kwargs={'slug': cls.main_service.slug})
        cls.download = DownloadFactory(service=cls.main_service)

    def test_response_status_code(self):
        self.assert_status_code(self.url)

    def test_correct_template_used(self):
        self.assert_template_used(
            self.url, 'components/service/partials/service-detail.html'
        )

    def test_context_contains_main_service(self):
        response = self.client.get(self.url)
        self.assertIn('service', response.context)
        self.assertEqual(response.context['service'], self.main_service)

    def test_context_contains_correct_other_services(self):
        response = self.client.get(self.url)
        expected_services = Service.objects.exclude(id=self.main_service.id).order_by(
            'id'
        )
        self.assertQuerysetEqual(
            response.context['services'].order_by('id'),
            expected_services,
            transform=lambda x: x,
        )

    def test_other_services_are_unique(self):
        response = self.client.get(self.url)
        service_ids = [s.id for s in response.context['services']]
        self.assertEqual(len(service_ids), len(set(service_ids)))

    def test_view_raises_404_for_invalid_service(self):
        bad_url = reverse_lazy('service-detail', kwargs={'slug': 'non-existent-slug'})
        response = self.client.get(bad_url)
        self.assertEqual(response.status_code, 404)

    def test_template_renders_service_name(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.main_service.name)

    def test_context_contains_download(self):
        response = self.client.get(self.url)
        downloads_count = self.main_service.downloads.count()
        self.assertEqual(downloads_count, 1)
        self.assertContains(response, self.download.title)

    def test_context_not_contains_other_service_download(self):
        unrelated_serive = ServiceFactory()
        unlrelated_download = DownloadFactory(service=unrelated_serive)
        context_downloads = self.main_service.downloads.all()
        self.assertNotIn(unlrelated_download, context_downloads)

    def test_view_with_no_downloads(self):
        Download.objects.all().delete()
        context_downloads = self.main_service.downloads.all()
        self.assertEqual(len(context_downloads), 0)

    # other model data context need to be added after testing
