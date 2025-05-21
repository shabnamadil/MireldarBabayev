from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel
from utils.validators.validate_phone import validate_phone_value


class Contact(BaseModel):
    first_name = models.CharField(
        _("First name"),
        max_length=20,
        help_text=_("The content length is a maximum of 20."),
    )
    last_name = models.CharField(
        _("Last name"),
        max_length=20,
        help_text=_("The content length is a maximum of 20."),
    )
    email = models.EmailField(
        _("Email"),
        error_messages={
            "invalid": _("Enter a valid email address."),
        },
    )
    phone = models.CharField(
        _("Phone number"),
        max_length=17,
        help_text=_("Only numeric values"),
        validators=[validate_phone_value],
    )
    message = models.TextField(_("Message"))

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
        indexes = [models.Index(fields=["created_at"])]
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return _("Message from %(first_name)s %(last_name)s") % {
            "first_name": self.first_name,
            "last_name": self.last_name,
        }
