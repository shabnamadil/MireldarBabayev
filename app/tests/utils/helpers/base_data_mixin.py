from django.core.exceptions import ValidationError


class BaseDataMixin:

    def assert_invalid_data(self, instance, field_name, fake_file):
        """Test that an invalid image raises a validation error."""
        setattr(instance, field_name, fake_file)
        with self.assertRaises(ValidationError):
            instance.full_clean()
