from django.test import TestCase

from apps.core.models import Contact
from django.core.exceptions import ValidationError

class TestContactModel(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.contact = Contact.objects.create(
            first_name='First name',
            last_name='Last name',
            email='test@gmail.com',
            phone='1234567890',
            message='Test message'
        )

    def test_str_method(self):
        self.assertEqual(str(self.contact), "First name Last name-dən mesaj")

    def test_email(self):
        invalid_emails = ['test', 'test@', 'test.com', 'test@.com', 'test@com']
        for email in invalid_emails:
            with self.assertRaises(ValidationError):
                self.contact.email = email
                self.contact.full_clean()

    def test_phone(self):
        invalid_phones = ['123', 'asdfgh', '12345678ty', '12345678901234567890']
        for phone in invalid_phones:
            with self.assertRaises(ValidationError):
                self.contact.phone = phone
                self.contact.full_clean()