from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel


class IP(BaseModel):
    view_ip = models.GenericIPAddressField(_("IP address"), editable=False)

    class Meta:
        verbose_name = _("IP address")
        verbose_name_plural = _("IP addresses")

    def __str__(self) -> str:
        return self.view_ip

    def save(self, *args, **kwargs):
        if self.pk and self.view_ip != IP.objects.get(pk=self.pk).view_ip:
            raise ValidationError(_("The 'view_ip' field cannot be changed."))
        super().save(*args, **kwargs)
