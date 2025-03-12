from django.core.validators import (
    MinLengthValidator,
)
from django.db import models

from utils.helpers.validate_google_map import (
    GoogleMapValidationError,
)
from utils.helpers.validate_phone import (
    PhoneValidationError,
)
from utils.helpers.validate_social_media import (
    validate_facebook,
    validate_instagram,
    validate_linkedin,
    validate_tiktok,
    validate_twitter,
    validate_youtube,
)
from utils.helpers.validate_work_hours import (
    WorkHourValidationError,
)
from utils.models.singleton import SingletonModel


class SiteSettings(SingletonModel):
    site_name = models.CharField(
        max_length=100,
        verbose_name="Site Name",
        validators=[MinLengthValidator(30)],
        help_text="Kontentin uzunluğu maksimum 100-dür.",
    )
    logo = models.ImageField(upload_to="logos/", verbose_name="Site Logo")
    favicon = models.ImageField(upload_to="favicons/", verbose_name="Favicon")
    location = models.CharField(
        "Məkan", max_length=100, help_text="Kontentin uzunluğu maksimum 100-dür."
    )
    number = models.CharField(
        "Əlaqə nömrəsi",
        max_length=17,
        help_text="Yalnız rəqəm daxil edin. Məsələn: +994123456789",
        validators=[PhoneValidationError],
    )
    email = models.EmailField("Email ünvanı")
    work_hours = models.CharField(
        "İş saatları",
        max_length=13,
        validators=[WorkHourValidationError],
        help_text="Kontentin uzunluğu maksimum 13-dür. Nümunə: 09:00 - 18:00",
    )
    map_url = models.CharField(
        "Xəritə",
        max_length=500,
        validators=[GoogleMapValidationError],
        help_text='Zəhmət olmasa, google məkanınızın "iframe" contentindən "src" attributunu daxil edin.',
    )
    facebook = models.URLField(
        "Facebook hesab linki", null=True, blank=True, validators=[validate_facebook]
    )
    youtube = models.URLField(
        "YouTube hesab linki", null=True, blank=True, validators=[validate_youtube]
    )
    twitter = models.URLField(
        "Twitter hesab linki", null=True, blank=True, validators=[validate_twitter]
    )
    instagram = models.URLField(
        "Instagram hesab linki", null=True, blank=True, validators=[validate_instagram]
    )
    linkedin = models.URLField(
        "LinkedIn hesab linki", null=True, blank=True, validators=[validate_linkedin]
    )
    tiktok = models.URLField(
        "TikTok hesab linki", null=True, blank=True, validators=[validate_tiktok]
    )
    footer_description = models.TextField("Footer hissədə göstəriləcək mətn")

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name
