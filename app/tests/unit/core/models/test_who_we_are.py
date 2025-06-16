from django.utils.translation import gettext_lazy as _

from apps.core.models import WhoWeAre
from tests.utils.helpers import BaseValidationTest


class TestWhoWeAreModel(BaseValidationTest):

    def test_who_we_are_str_returns_valid_string(self):
        instance = WhoWeAre()
        self.assertEqual(str(instance), str(_("Biz kimik?")))
