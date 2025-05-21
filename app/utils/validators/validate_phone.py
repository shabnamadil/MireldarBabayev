import re

from django.core.exceptions import ValidationError


def validate_phone_value(value):
    if not re.match(r"^\+?1?\d{9,15}$", value):
        raise ValidationError(f"{value} is not a valid phone number")
