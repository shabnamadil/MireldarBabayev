import re

from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_time_format(value):
    """Validates that the time format is HH:MM - HH:MM."""
    pattern = r"^(\d{2}):(\d{2}) - (\d{2}):(\d{2})$"
    match = re.match(pattern, value)
    if not match:
        raise ValidationError(f"{value} is not a valid work hour format.")
    return match.groups()  # Return groups instead of match object


def validate_hour_minute(hour, minute):
    """Ensures hours (00-23) and minutes (00-59) are valid."""
    if not (0 <= hour <= 23):
        raise ValidationError("Hours must be between 00 and 23.")
    elif not (0 <= minute <= 59):
        raise ValidationError("Minutes must be between 00 and 59.")


def validate_time_order(start_hour, start_minute, end_hour, end_minute):
    """Ensures start time is before end time."""
    start_time = f"{start_hour:02}:{start_minute:02}"
    end_time = f"{end_hour:02}:{end_minute:02}"

    if start_time >= end_time:
        raise ValidationError(
            f"Start time must be before end time: {start_time} - {end_time}"
        )


def validate_work_hours(value):
    """Validates time format, range, and order."""
    start_hour, start_minute, end_hour, end_minute = map(
        int, validate_time_format(value)
    )

    validate_hour_minute(start_hour, start_minute)
    validate_hour_minute(end_hour, end_minute)
    validate_time_order(start_hour, start_minute, end_hour, end_minute)

    return value  # Always return the validated value


def validate_start_end_times(start, end):
    """Validates start and end time logic."""
    if start and end:
        if start == end:
            raise ValidationError("Start and End time cannot be the same.")
        elif end < start:
            raise ValidationError("The end time must be after the start time.")


def validate_future_time(value, field_name):
    """Ensures the given time is in the future."""
    local_time = timezone.localtime(timezone.now())
    if value and value < local_time:
        raise ValidationError({field_name: "The start time must be in the future."})
