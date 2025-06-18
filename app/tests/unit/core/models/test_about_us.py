from django.utils.translation import gettext_lazy as _

from apps.core.models import AboutUs
from tests.utils.helpers import BaseValidationTest


class TestAboutUsModel(BaseValidationTest):

    def test_about_us_str_returns_valid_string(self):
        instance = AboutUs()
        self.assertEqual(str(instance), str(_("About Us Information")))
