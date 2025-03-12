import re

from django.core.exceptions import ValidationError


def WorkHourValidationError(value):
    pattern = r"^(\d{2}):(\d{2}) - (\d{2}):(\d{2})$"
    match = re.match(pattern, value)

    if not match:
        raise ValidationError(f"{value} is not a valid work hour format.")

    (
        start_hour,
        start_minute,
        end_hour,
        end_minute,
    ) = map(int, match.groups())

    if not (0 <= start_hour <= 23 and 0 <= end_hour <= 23):
        raise ValidationError(f"Hours must be between 00 and 23: {value}")

    if not (0 <= start_minute <= 59 and 0 <= end_minute <= 59):
        raise ValidationError(f"Minutes must be between 00 and 59: {value}")

    if (
        f"{start_hour:02}:{start_minute:02}"
        >= f"{end_hour:02}:{end_minute:02}"
    ):
        raise ValidationError(f"Start time must be before end time: {value}")
