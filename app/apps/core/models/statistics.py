from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel
from utils.validators.validate_image import validate_image_size as ImageSizeValidator
from utils.validators.validate_png import validate_png_content as PngContentValidator
from utils.validators.validate_png import (
    validate_png_extension as PngExtensionValidator,
)


class StatisticalIndicator(BaseModel):
    png = models.ImageField(
        _("Indicator png"),
        upload_to="statistics/",
        help_text=_("Please upload a PNG file."),
        validators=[
            ImageSizeValidator,
            PngExtensionValidator,
            PngContentValidator,
        ],
    )
    value = models.IntegerField(
        _("Statistical indicator value"),
    )
    name = models.CharField(
        _("Statistical indicator name"),
        max_length=50,
        unique=True,
        help_text=_("The content length is a maximum of 50."),
    )

    class Meta:
        verbose_name = _("Statistical Indicator")
        verbose_name_plural = _("Statistical Indicators")
        indexes = [models.Index(fields=["created_at"])]
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name
