from apps.core.models import Newsletter
from tests.utils.factories import NewsletterFactory
from tests.utils.helpers import (
    BaseValidationTest,
)


class TestNewsletterModelIntegration(BaseValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = NewsletterFactory
        cls.object = cls.factory()
        cls.model = Newsletter

    def test_email_required(self):
        self.assert_required_field(self.object, "email")

    def test_email_unique(self):
        self.assert_unique_field(self.model, "email", self.object.email)

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_email_saved_correctly(self):
        self.assert_model_instance(self.object, "email", self.object.email)

    def test_object_is_instance_of_newsletter(self):
        self.assertIsInstance(self.object, self.model)

    def test_invalid_email_raises_validation_error(self):
        self.assert_invalid_email(self.object)

    def test_newsletters_are_ordered_by_created_at_desc(self):
        self.assert_ordering(self.factory, self.model)
