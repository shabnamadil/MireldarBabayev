from apps.core.models import Newsletter
from tests.utils.helpers import BaseValidationTest


class TestNewsletterModel(BaseValidationTest):

    def test_newsletter_returns_email(self):
        self.assert_str_output(Newsletter, "email", "Test email")
