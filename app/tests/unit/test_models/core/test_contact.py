from apps.core.models import Contact
from utils.tests.base import BaseValidationTest


class TestContactModel(BaseValidationTest):
    
    @classmethod
    def setUpTestData(cls):
        cls.contact = Contact.objects.create(
            first_name='First name',
            last_name='Last name',
            email='test@gmail.com',
            phone='1234567890',
            message='Test message'
        )

    def test_contact_model(self):
        self.assert_model_instance(Contact, 'first_name', 'First name')
        self.assert_model_instance(Contact, 'last_name', 'Last name')
        self.assert_model_instance(Contact, 'email', 'test@gmail.com')
        self.assert_model_instance(Contact, 'phone', '1234567890')
        self.assert_model_instance(Contact, 'message', 'Test message')

    def test_str_method(self):
        self.assert_str_method(self.contact, 'First name Last name-dən mesaj')

    def test_email(self):
        self.assert_invalid_email(self.contact, email_field='email')

    def test_phone(self):
        self.assert_invalid_number(self.contact, number_field='phone')

    def test_phone_max_length(self):
        self.assert_max_length(self.contact, 'phone', 17)

    def test_first_name_max_length(self):
        self.assert_max_length(self.contact, 'first_name', 20)

    def test_last_name_max_length(self):
        self.assert_max_length(self.contact, 'last_name', 20)

    def test_object_count(self):
        self.assert_object_count(Contact, 1)

    def test_deletion(self):
        self.assert_object_deleted(Contact)