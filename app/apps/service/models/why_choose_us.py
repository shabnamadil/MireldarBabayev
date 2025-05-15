from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel
from utils.validators.validate_image import validate_image_size as ImageSizeValidator
from utils.validators.validate_png import validate_png_content as PngContentValidator
from utils.validators.validate_png import (
    validate_png_extension as PngExtensionValidator,
)


class WhyChooseUs(BaseModel):
    title = models.CharField(
        _('Title'),
        max_length=30,
        unique=True,
        help_text=_('The content length is a maximum of 30.'),
    )
    short_description = models.TextField(
        _('Short description'),
        unique=True,
        validators=[MinLengthValidator(50), MaxLengthValidator(60)],
        help_text=_('The content length is a maximum of 60, minimum of 30.'),
    )
    png = models.FileField(
        _('PNG file'),
        upload_to='why_choose_us/',
        validators=[ImageSizeValidator, PngContentValidator, PngExtensionValidator],
        help_text=_('Please upload a PNG file.'),
    )

    class Meta:
        verbose_name = _('Why Choose Us')
        verbose_name_plural = _('Why Choose Us')
        ordering = ['-created_at']
        indexes = [models.Index(fields=['-created_at'])]

    def __str__(self) -> str:
        return self.title
