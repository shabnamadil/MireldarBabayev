from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.helpers.slugify import custom_slugify
from utils.models.base_model import BaseModel


class Tag(BaseModel):
    name = models.CharField(
        _("Tag name"),
        max_length=80,
        unique=True,
        help_text=_("The content length is a maximum of 80."),
    )
    slug = models.SlugField(
        _("Slug"),
        null=True,
        blank=True,
        help_text=_("Leave this field blank. It will be filled automatically."),
        max_length=500,
    )

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.name)
        super().save(*args, **kwargs)
