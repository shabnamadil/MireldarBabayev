from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from PIL import Image


def validate_png_extension(file):
    file_name = file.name  # Get filename from file object
    if not file_name.lower().endswith('.png'):
        raise ValidationError(_('Only PNG files are accepted.'))


def validate_png_content(file):
    try:
        image = Image.open(file)
        image.verify()  # Ensures it's an image file, not just named .png
        file.seek(0)  # Reset file pointer for further use

        if image.format != 'PNG':
            raise ValidationError(_('Uploaded file is not a valid PNG image.'))
    except Exception:
        raise ValidationError(_('Upload a valid PNG image.'))
