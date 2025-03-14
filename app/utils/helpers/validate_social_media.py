import re

from django.core.exceptions import ValidationError


def validate_facebook(value):
    pattern = r'^https?://(www\.)?facebook\.com/.*$'
    if not re.match(pattern, value):
        raise ValidationError(
            "Invalid Facebook URL. Please enter a valid Facebook link."
        )


def validate_youtube(value):
    pattern = r'^https?://(www\.)?youtube\.com/.*$'
    if not re.match(pattern, value):
        raise ValidationError(
            "Invalid YouTube URL. Please enter a valid YouTube link."
        )


def validate_twitter(value):
    pattern = r'^https?://(www\.)?twitter\.com/.*$'
    if not re.match(pattern, value):
        raise ValidationError(
            "Invalid Twitter URL. Please enter a valid Twitter link."
        )


def validate_instagram(value):
    pattern = r'^https?://(www\.)?instagram\.com/.*$'
    if not re.match(pattern, value):
        raise ValidationError(
            "Invalid Instagram URL. Please enter a valid Instagram link."
        )


def validate_linkedin(value):
    pattern = r'^https?://(www\.)?linkedin\.com/.*$'
    if not re.match(pattern, value):
        raise ValidationError(
            "Invalid LinkedIn URL. Please enter a valid LinkedIn link."
        )


def validate_tiktok(value):
    pattern = r'^https?://(www\.)?tiktok\.com/.*$'
    if not re.match(pattern, value):
        raise ValidationError(
            "Invalid TikTok URL. Please enter a valid TikTok link."
        )
