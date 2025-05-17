from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField
from utils.helpers.slugify import custom_slugify
from utils.models.base_model import BaseModel
from utils.validators.validate_image import (
    validate_image_content as ImageContentValidator,
)
from utils.validators.validate_image import (
    validate_image_extension as ImageExtensionValidator,
)
from utils.validators.validate_image import validate_image_size as ImageSizeValidator
from utils.validators.validate_png import validate_png_content as PngContentValidator
from utils.validators.validate_png import (
    validate_png_extension as PngExtensionValidator,
)


class Service(BaseModel):
    COLOR_CHOICES = (
        ('yellow', _('yellow')),
        ('green', _('green')),
        ('blue', _('blue')),
    )
    name = models.CharField(
        _('Service name'),
        max_length=30,
        unique=True,
        help_text=_('The content length is a maximum of 30.'),
    )
    short_description = models.TextField(
        _('Short description'),
        validators=[MinLengthValidator(145), MaxLengthValidator(160)],
        help_text=_('The content length is a maximum of 160, minimum of 145.'),
    )
    png = models.ImageField(
        _('PNG file'),
        upload_to='services/png/',
        help_text=_('Please upload a PNG file.(94x74px)'),
        validators=[ImageSizeValidator, PngExtensionValidator, PngContentValidator],
    )
    image = models.ImageField(
        _('Main photo'),
        upload_to='services/images/',
        validators=[ImageExtensionValidator, ImageSizeValidator, ImageContentValidator],
        help_text=_('Please upload a PNG or JPG file'),
    )
    title = models.CharField(
        _('Title'),
        unique=True,
        max_length=60,
        validators=[MinLengthValidator(30)],
        help_text=_('The content length is a maximum of 60, minimum of 30.'),
    )
    content = RichTextUploadingField(
        _('Content'),
        help_text=_('The content length is a maximum of 1000, minimum of 300.'),
        validators=[MinLengthValidator(300), MaxLengthValidator(1000)],
    )
    background_color = models.CharField(
        _('Background color'), choices=COLOR_CHOICES, default='blue', max_length=20
    )
    slug = models.SlugField(
        _('Slug'),
        null=True,
        blank=True,
        help_text=_('Leave blank to auto-generate.'),
        max_length=500,
    )

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
        ordering = ['-created_at']
        indexes = [models.Index(fields=['-created_at'])]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('service-detail', args=[self.slug])

    def __str__(self) -> str:
        return self.name
