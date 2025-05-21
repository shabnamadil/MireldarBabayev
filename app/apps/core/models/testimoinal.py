from django.core.validators import (
    MaxLengthValidator,
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel
from utils.validators.validate_image import (
    validate_image_content as ImageContentValidator,
)
from utils.validators.validate_image import (
    validate_image_extension as ImageExtensionValidator,
)
from utils.validators.validate_image import validate_image_size as ImageSizeValidator


class Testimoinal(BaseModel):
    client_image = models.ImageField(
        _("Client image"),
        upload_to="testimonials/",
        help_text="Kindly upload a photo for the About page. Image size shoud not exceed 2mb. (170x170px)",
        validators=[
            ImageSizeValidator,
            ImageContentValidator,
            ImageExtensionValidator,
        ],
    )
    client_full_name = models.CharField(
        _("Client full name"),
        max_length=20,
        help_text=_("The content length is a maximum of 20."),
    )
    client_profession = models.CharField(
        _("Client profession"),
        max_length=100,
        help_text=_("The content length is a maximum of 100."),
    )
    client_comment = models.TextField(
        _("Comment"),
        validators=[MinLengthValidator(150), MaxLengthValidator(155)],
    )
    star = models.IntegerField(
        _("Stars given by client"),
        help_text=_("Points between 1 and 5"),
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")
        indexes = [models.Index(fields=["created_at"])]
        ordering = ("-created_at",)

    @property
    def star_range(self):
        return range(self.star)

    def __str__(self) -> str:
        return _("Comment by %(client_full_name)s") % {
            "client_full_name": self.client_full_name
        }
