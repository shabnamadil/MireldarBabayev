from apps.core.models import Newsletter
from utils.tests.base import BaseValidationTest


class TestNewsletterModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.newsletter = Newsletter.objects.create(email="test@gmail.com")

    def test_newsletter_model(self):
        self.assert_model_instance(Newsletter, "email", "test@gmail.com")

    def test_str_method(self):
        self.assert_str_method(self.newsletter, "test@gmail.com")

    def test_email_unique(self):
        self.assert_unique_field(Newsletter, "email", "test@gmail.com")

    def test_email(self):
        self.assert_invalid_email(self.newsletter, email_field="email")

    def test_object_count(self):
        self.assert_object_count(Newsletter, 1)

    def test_deletion(self):
        self.assert_object_deleted(Newsletter)
