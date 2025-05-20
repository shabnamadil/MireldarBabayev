import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_facebook(value):
    pattern = r"^https?://(www\.)?facebook\.com/.*$"
    if not re.match(pattern, value):
        raise ValidationError(
            _("Invalid Facebook URL. Please enter a valid Facebook link.")
        )


def validate_youtube(value):
    pattern = r"^https?://(www\.)?youtube\.com/.*$"
    if not re.match(pattern, value):
        raise ValidationError(
            _("Invalid YouTube URL. Please enter a valid YouTube link.")
        )


def validate_twitter(value):
    pattern = r"^https?://(www\.)?twitter\.com/.*$"
    if not re.match(pattern, value):
        raise ValidationError(
            _("Invalid Twitter URL. Please enter a valid Twitter link.")
        )


def validate_instagram(value):
    pattern = r"^https?://(www\.)?instagram\.com/.*$"
    if not re.match(pattern, value):
        raise ValidationError(
            _("Invalid Instagram URL. Please enter a valid Instagram link.")
        )


def validate_linkedin(value):
    pattern = r"^https?://(www\.)?linkedin\.com/.*$"
    if not re.match(pattern, value):
        raise ValidationError(
            _("Invalid LinkedIn URL. Please enter a valid LinkedIn link.")
        )


def validate_tiktok(value):
    pattern = r"^https?://(www\.)?tiktok\.com/.*$"
    if not re.match(pattern, value):
        raise ValidationError(
            _("Invalid TikTok URL. Please enter a valid TikTok link.")
        )


def validate_youtube_video_id(value):
    pattern = r"^[a-zA-Z0-9_-]{11}$"
    if not re.match(pattern, value):
        raise ValidationError(
            _(
                "Enter a valid YouTube video ID (11 characters, alphanumeric with _ or -)."
            )
        )
