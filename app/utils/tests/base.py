from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError


class BaseValidationTest(TestCase):

    def assert_invalid_email(self, instance, email_field='email'):
        """Test that an invalid email raises a validation error."""
        invalid_emails = ['invalid_email', 'user@.com', '@gmail.com', 'test', 'test@', 'test.com', 'test@.com', 'test@com']
        for email in invalid_emails:
            setattr(instance, email_field, email)
            with self.assertRaises(ValidationError):
                instance.full_clean()

    def assert_invalid_number(self, instance, number_field=None):
        """Test that an invalid number raises a validation error."""
        invalid_numbers = ['123', '-1234567890', 'asdfgh', '12345678ty', '12345678901234567890']
        for number in invalid_numbers:
            setattr(instance, number_field, number)
            with self.assertRaises(ValidationError):
                instance.full_clean()

    def assert_singleton(self, model):
        """Test that a model is a singleton."""
        with self.assertRaises(IntegrityError):
            model.objects.create()

    def assert_unique_field(self, model, field, value):
        """Test that a field is unique."""
        with self.assertRaises(IntegrityError):
            model.objects.create(**{field: value})

    def assert_object_count(self, model, count):
        """Test that the object count is equal to the given count."""
        self.assertEqual(model.objects.count(), count)

    def assert_str_method(self, instance, expected_str):
        """Test that the __str__ method returns the expected string."""
        self.assertEqual(str(instance), expected_str)

    def assert_max_length(self, instance, field, length):
        """Test that invalid length raises a validation error."""
        setattr(instance, field, 'a' * (length + 1))
        with self.assertRaises(ValidationError):
            instance.full_clean()

    def assert_min_length(self, instance, field, length):
        """Test that invalid length raises a validation error."""
        setattr(instance, field, 'a' * (length - 1))
        with self.assertRaises(ValidationError):
            instance.full_clean()

    def assert_field_type(self, instance, field, field_type):
        """Test that invalid type raises a validation error."""
        setattr(instance, field, field_type)
        with self.assertRaises(ValidationError):
            instance.full_clean()

    def assert_model_instance(self, model, field, value):
        """Test that the model instance is equal to the given value."""
        model_instance = model.objects.first()
        self.assertEqual(getattr(model_instance, field), value)
