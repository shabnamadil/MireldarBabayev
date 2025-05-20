from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel


class BaseSeoDetailModel(BaseModel):
    """All seo detail models inherit this model"""

    meta_description = models.TextField(
        _("Meta description"),
        validators=[MaxLengthValidator(160), MinLengthValidator(50)],
        help_text=_("The content length must be between 50 and 160 characters."),
    )
    meta_keywords = models.TextField(
        _("Meta keywords"),
        validators=[MaxLengthValidator(160), MinLengthValidator(50)],
        help_text=_("The content length must be between 50 and 160 characters."),
    )
    og_description = models.TextField(
        _("Og description"),
        validators=[MaxLengthValidator(160), MinLengthValidator(50)],
        help_text=_("The content length must be between 50 and 160 characters."),
    )

    class Meta:
        abstract = True
