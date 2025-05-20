from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase
from django.utils import timezone

User = get_user_model()


class BaseValidationTest(TestCase):

    def assert_invalid_email(self, instance, email_field="email"):
        """Test that an invalid email raises a validation error."""
        invalid_emails = [
            "invalid_email",
            "user@.com",
            "@gmail.com",
            "test",
            "test@",
            "test.com",
            "test@.com",
            "test@com",
        ]
        for email in invalid_emails:
            setattr(instance, email_field, email)
            with self.assertRaises(ValidationError):
                instance.full_clean()

    def assert_invalid_number(self, instance, number_field=None):
        """Test that an invalid number raises a validation error."""
        invalid_numbers = [
            "123",
            "-1234567890",
            "asdfgh",
            "12345678ty",
            "12345678901234567890",
        ]
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

    def assert_object_deleted(self, model):
        """Test that the object is deleted."""
        model.objects.first().delete()
        self.assert_object_count(model, 0)

    def assert_str_output(self, model_class, field_name, expected_str):
        """Test that the __str__ method returns the expected string."""
        instance = model_class(**{field_name: expected_str})
        self.assertEqual(str(instance), expected_str)

    def assert_max_length(self, instance, field, length):
        """Test that invalid length raises a validation error."""
        setattr(instance, field, "a" * (length + 1))
        with self.assertRaises(ValidationError):
            instance.full_clean()

    def assert_min_length(self, instance, field, length):
        """Test that invalid length raises a validation error."""
        setattr(instance, field, "a" * (length - 1))
        with self.assertRaises(ValidationError):
            instance.full_clean()

    def assert_field_type(self, instance, field, field_type):
        """Test that invalid type raises a validation error."""
        setattr(instance, field, field_type)
        with self.assertRaises(ValidationError):
            instance.full_clean()

    def assert_model_instance(self, instance, field, value):
        """Assert that the given model instance field matches the expected value from the database."""
        instance.refresh_from_db()
        self.assertEqual(getattr(instance, field), value)

    def assert_valid_social_media_urls(self, instance, url_field, valid_url):
        """Test that valid URL does not raise a validation error."""
        setattr(instance, url_field, valid_url)
        instance.full_clean()

    def assert_invalid_social_media_urls(self, instance, url_field):
        """Test that invalid URL raises a validation error."""
        invalid_urls = [
            "invalid_url",  # Not a URL
            "www.invalid.com",  # Missing scheme (http:// or https://)
            "http://invalid.com",  # Not a social media link
            "https://invalid.com",  # Not a social media link
        ]
        for url in invalid_urls:
            setattr(instance, url_field, url)
            with self.assertRaises(ValidationError):
                instance.full_clean()

    def assert_required_field(self, instance, field):
        """Test that a required field raises a validation error."""
        setattr(instance, field, None)
        with self.assertRaises(ValidationError):
            instance.full_clean()

    def assert_slug_auto_generation(self, instance, slug_field):
        """Test that the slug is auto-generated."""
        setattr(instance, slug_field, None)
        instance.save()
        self.assertIsNotNone(getattr(instance, slug_field))
        self.assertNotEqual(getattr(instance, slug_field), "")

    def assert_ordering(self, factory, model):
        s1 = factory(created_at=timezone.now() - timedelta(days=1))
        s2 = factory(created_at=timezone.now())

        objects = model.objects.filter(id__in=[s1.id, s2.id])
        self.assertEqual(list(objects), [s2, s1])

    def assert_status_code(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def assert_template_used(self, url, template):
        response = self.client.get(url)
        self.assertTemplateUsed(response, template)

    def assert_all_objects_in_context(self, url, context_key, objects):
        response = self.client.get(url)
        self.assertIn(context_key, response.context)

        for obj in objects:
            with self.subTest(obj=obj):
                self.assertIn(obj, response.context[context_key])

    def assert_view_returns_all_objects(self, url, context_key, model):
        response = self.client.get(url)
        self.assertQuerysetEqual(
            response.context[context_key].order_by("id"),
            model.objects.all().order_by("id"),
            transform=lambda x: x,  # compare actual objects, not repr()
        )

    def assert_view_without_context_data(self, model, url, context_key):
        model.objects.all().delete()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context[context_key], [])
