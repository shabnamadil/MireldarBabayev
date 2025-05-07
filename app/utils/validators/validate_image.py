from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_image_size(value):
    max_size_mb = 2
    if value.size > max_size_mb * 1024 * 1024:
        raise ValidationError(_(f'Image size should not exceed {max_size_mb} MB.'))


def validate_image_extension(file, allowed_extensions=[".jpg", ".png", ".jpeg"]):
    file_name = file.name  # Get filename from file object
    if not any(file_name.lower().endswith(ext) for ext in allowed_extensions):
        raise ValidationError(_('Only JPG, PNG, and JPEG files are accepted.'))
