from django.db import models
from django.core.exceptions import ValidationError

from utils.models.base_model import BaseModel


class IP(BaseModel):
    view_ip = models.GenericIPAddressField(
        'IP ünvanı', 
        editable=False
    )

    class Meta:
        verbose_name = ('IP ünvanı')
        verbose_name_plural = ('IP ünvanları')

    def __str__(self) -> str:
        return self.view_ip
    
    def save(self, *args, **kwargs):
        if self.pk and self.view_ip != IP.objects.get(pk=self.pk).view_ip:
            raise ValidationError("The 'view_ip' field cannot be changed.")
        super().save(*args, **kwargs)