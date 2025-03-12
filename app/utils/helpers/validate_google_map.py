import re

from django.core.exceptions import ValidationError


def GoogleMapValidationError(value):
    pattern = r"^https:\/\/www\.google\.com\/maps\/embed\?.+"
    if not re.match(pattern, value):
        raise ValidationError(f"{value} is not a valid google map url")
