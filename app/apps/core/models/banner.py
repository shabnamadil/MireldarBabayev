from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel
from utils.validators.validate_image import validate_image_size as ImageSizeValidator
from utils.validators.validate_png import validate_png_content as PngContentValidator
from utils.validators.validate_png import (
    validate_png_extension as PngExtensionValidator,
)
from utils.validators.validate_social_media import (
    validate_youtube_video_id as VideoIdValidator,
)


class Banner(BaseModel):
    title = models.CharField(
        _("Title"),
        max_length=100,
        unique=True,
        help_text=_("The content length is a maximum of 100."),
    )
    subtitle = models.CharField(
        _("Subtitle"),
        max_length=100,
        unique=True,
        help_text=_("The content length is a maximum of 100."),
    )
    description = models.TextField(_("Short description"), unique=True)
    png = models.ImageField(
        _("Banner photo"),
        upload_to="banner/",
        help_text=_("Please upload a PNG file.(720x726px)"),
        validators=[
            ImageSizeValidator,
            PngExtensionValidator,
            PngContentValidator,
        ],
    )
    video_id = models.CharField(
        _("Video ID"),
        help_text=_(
            'Example: From the link "https://www.youtube.com/watch?v=MKG_6BqnhpI", only "MKG_6BqnhpI" should be entered.'
        ),
        unique=True,
        max_length=11,
        validators=[VideoIdValidator],
    )

    class Meta:
        verbose_name = _("Banner")
        verbose_name_plural = _("Banners")
        indexes = [models.Index(fields=["created_at"])]
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title
