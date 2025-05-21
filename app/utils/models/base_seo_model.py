from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models.singleton import SingletonModel
from utils.validators.validate_image import (
    validate_image_content as ImageContentValidator,
)
from utils.validators.validate_image import (
    validate_image_extension as ImageExtensionValidator,
)
from utils.validators.validate_image import validate_image_size as ImageSizeValidator

from .base_seo_detail import BaseSeoDetailModel
from .singleton import SingletonModel


class BaseSeoModel(SingletonModel, BaseSeoDetailModel):
    """All seo models inherit this model"""

    meta_title = models.CharField(
        _("Meta title"),
        max_length=60,
        validators=[
            MinLengthValidator(30),
        ],
        help_text=_("The content length must be between 30 and 60 characters."),
    )
    og_title = models.CharField(
        _("Og title"),
        max_length=60,
        validators=[MinLengthValidator(30)],
        help_text=_("The content length must be between 30 and 60 characters."),
    )
    og_image = models.ImageField(
        _("Og image"),
        null=True,
        blank=True,
        upload_to="seo-images/",
        validators=[
            ImageSizeValidator,
            ImageContentValidator,
            ImageExtensionValidator,
        ],
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.meta_title
