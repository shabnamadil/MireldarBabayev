from django.core.exceptions import ValidationError


class BaseImageMixin:

    def assert_invalid_image(self, instance, image_field, fake_file):
        """Test that an invalid image raises a validation error."""
        setattr(instance, image_field, fake_file)
        with self.assertRaises(ValidationError):
            instance.full_clean()
