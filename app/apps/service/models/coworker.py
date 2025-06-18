from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel
from utils.validators.validate_image import validate_image_size as ImageSizeValidator
from utils.validators.validate_png import validate_png_content as PngContentValidator
from utils.validators.validate_png import (
    validate_png_extension as PngExtensionValidator,
)


class Coworker(BaseModel):
    name = models.CharField(
        _("Company name"),
        max_length=100,
        unique=True,
        help_text=_("The content length is a maximum of 100."),
    )
    png = models.FileField(
        _("Logo"),
        upload_to="coworkers/",
        help_text=_("Please upload a PNG file."),
        validators=[
            ImageSizeValidator,
            PngContentValidator,
            PngExtensionValidator,
        ],
    )

    class Meta:
        verbose_name = _("Coworker")
        verbose_name_plural = _("Coworkers")
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["-created_at"])]

    def __str__(self) -> str:
        return self.name
