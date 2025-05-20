from django.utils.translation import gettext_lazy as _

from apps.core.models import Contact
from tests.utils.factories import ContactFactory
from tests.utils.helpers import (
    BaseValidationTest,
)


class TestContactModelIntegration(BaseValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = ContactFactory
        cls.object = cls.factory()
        cls.model = Contact

    def test_contact_str_returns_translated_name(self):
        expected = _("Message from %(first_name)s %(last_name)s") % {
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
        }
        self.assertEqual(str(self.object), expected)

    def test_first_name_max_length(self):
        self.assert_max_length(self.object, "first_name", 20)

    def test_last_name_max_length(self):
        self.assert_max_length(self.object, "last_name", 20)

    def test_phone_max_length(self):
        self.assert_max_length(self.object, "phone", 17)

    def test_first_name_required(self):
        self.assert_required_field(self.object, "first_name")

    def test_last_name_required(self):
        self.assert_required_field(self.object, "last_name")

    def test_email_required(self):
        self.assert_required_field(self.object, "email")

    def test_phone_required(self):
        self.assert_required_field(self.object, "phone")

    def test_message_required(self):
        self.assert_required_field(self.object, "message")

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_fist_name_saved_correctly(self):
        self.assert_model_instance(self.object, "first_name", self.object.first_name)

    def test_last_name_saved_correctly(self):
        self.assert_model_instance(self.object, "last_name", self.object.last_name)

    def test_email_saved_correctly(self):
        self.assert_model_instance(self.object, "email", self.object.email)

    def test_phone_saved_correctly(self):
        self.assert_model_instance(self.object, "phone", self.object.phone)

    def test_message_saved_correctly(self):
        self.assert_model_instance(self.object, "message", self.object.message)

    def test_object_is_instance_of_contact(self):
        self.assertIsInstance(self.object, self.model)

    def test_invalid_email_raises_validation_error(self):
        self.assert_invalid_email(self.object)

    def test_invalid_phone_number_raises_validation_error(self):
        self.assert_invalid_number(self.object, "phone")
