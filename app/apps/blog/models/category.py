from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.helpers.slugify import custom_slugify
from utils.models.base_model import BaseModel


class Category(BaseModel):
    name = models.CharField(
        _("Category name"),
        max_length=150,
        unique=True,
        help_text=_("The content length is a maximum of 150."),
    )
    slug = models.SlugField(
        _("Slug"),
        null=True,
        blank=True,
        help_text=_("Leave blank to auto-generate."),
        max_length=500,
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.name)
        super().save(*args, **kwargs)
