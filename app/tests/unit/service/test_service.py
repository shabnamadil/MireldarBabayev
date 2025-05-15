from django.utils.translation import activate
from django.utils.translation import gettext as _

from apps.service.models import Service
from utils.tests.base import BaseValidationTest


class TestServiceModel(BaseValidationTest):

    def test_service_str_returns_name(self):
        self.assert_str_output(Service, 'name', 'Test service')

    def test_get_absolute_url_returns_correct_path(self):
        service = Service(slug="branding")
        activate("en")
        url = service.get_absolute_url()
        self.assertEqual(url, "/en/services/branding/")

    def test_meta_verbose_names(self):
        self.assertEqual(Service._meta.verbose_name, _("Service"))
        self.assertEqual(Service._meta.verbose_name_plural, _("Services"))

    def test_color_choices_labels_are_translated(self):
        choices = dict(Service.COLOR_CHOICES)
        for color in ["yellow", "green", "blue"]:
            self.assertIn(color, choices)
            self.assertTrue(callable(_))
