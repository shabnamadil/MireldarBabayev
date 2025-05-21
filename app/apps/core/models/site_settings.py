from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models.singleton import SingletonModel
from utils.validators.validate_google_map import GoogleMapValidationError
from utils.validators.validate_image import validate_image_size as ImageSizeValidator
from utils.validators.validate_phone import validate_phone_value
from utils.validators.validate_png import validate_png_content as PngContentValidator
from utils.validators.validate_png import (
    validate_png_extension as PngExtensionValidator,
)
from utils.validators.validate_social_media import (
    validate_facebook,
    validate_instagram,
    validate_linkedin,
    validate_tiktok,
    validate_twitter,
    validate_youtube,
)
from utils.validators.validate_time import (
    validate_work_hours as WorkHourValidationError,
)


class SiteSettings(SingletonModel):
    site_name = models.CharField(
        _("Site name"),
        max_length=100,
        validators=[MinLengthValidator(30)],
        help_text=_("The content length is a maximum of 100, minimum of 30."),
    )
    logo = models.ImageField(
        _('Logo'),
        upload_to='logos/',
        help_text=_("Please upload a PNG file."),
        validators=[
            ImageSizeValidator,
            PngExtensionValidator,
            PngContentValidator,
        ],
    )
    favicon = models.ImageField(
        _("Favicon"),
        upload_to='favicons/',
        help_text=_("Please upload a PNG file."),
        validators=[
            ImageSizeValidator,
            PngExtensionValidator,
            PngContentValidator,
        ],
    )
    location = models.CharField(
        _('Location'),
        max_length=100,
        help_text=_("The content length is a maximum of 100.")
    )
    number = models.CharField(
        _("Phone number"),
        max_length=17,
        help_text=_("Only numeric values"),
        validators=[validate_phone_value]
    )
    email = models.EmailField(
        _("Email")
    )
    work_hours = models.CharField(
        _("Work hours"),
        max_length=13,
        validators=[WorkHourValidationError],
        help_text='The content length is a maximum of 13. Example: 09:00 - 18:00'
    )
    map_url = models.CharField(
        _("Map"),
        max_length=500,
        validators=[GoogleMapValidationError],
        help_text="Please enter the 'src' attribute from the 'iframe' content of your Google location."
    )
    facebook = models.URLField(
        _("Facebook link"),
        null=True, blank=True,
        validators=[validate_facebook]
    )
    youtube = models.URLField(
        _("Youtube link"),
        null=True, blank=True,
        validators=[validate_youtube]
    )
    twitter = models.URLField(
        _("Twitter link"),
        null=True, blank=True,
        validators=[validate_twitter]
    )
    instagram = models.URLField(
        _("Instagram link"),
        null=True, blank=True,
        validators=[validate_instagram]
    )
    linkedin = models.URLField(
        _("Linkedin link"),
        null=True, blank=True,
        validators=[validate_linkedin]
    )
    tiktok = models.URLField(
        _("Tiktok link"),
        null=True, blank=True,
        validators=[validate_tiktok]
    )
    footer_description = models.TextField(
        _("Footer description"),
        validators=[MaxLengthValidator(200)]
    )

    class Meta:
        verbose_name = _("Site Setting")
        verbose_name_plural = _("Site Settings")

    def __str__(self):
        return self.site_name
