from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel


class Newsletter(BaseModel):
    email = models.EmailField(_("Email"), unique=True)

    class Meta:
        verbose_name = _("Newsletter")
        verbose_name_plural = _("Newsletters")
        indexes = [models.Index(fields=["created_at"])]
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.email
