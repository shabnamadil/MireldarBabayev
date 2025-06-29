from django.utils.translation import activate
from django.utils.translation import gettext as _

from apps.service.models import Service
from tests.utils.helpers import BaseValidationTest


class TestServiceModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.model = Service

    def test_service_str_returns_name(self):
        self.assert_str_output(self.model, "name", "Test service")

    def test_get_absolute_url_returns_correct_path(self):
        service = self.model(slug="branding")
        activate("en")
        url = service.get_absolute_url()
        self.assertEqual(url, "/en/services/branding/")

    def test_color_choices_labels_are_translated(self):
        choices = dict(self.model.COLOR_CHOICES)
        for color in ["yellow", "green", "blue"]:
            self.assertIn(color, choices)
            self.assertTrue(callable(_))
