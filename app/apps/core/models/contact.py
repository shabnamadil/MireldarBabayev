from django.db import models

from utils.models.base_model import BaseModel
from django.core.exceptions import ValidationError

import re

def validate_phone(value):
    if not re.match(r'^\+?1?\d{9,15}$', value):
        raise ValidationError(f'{value} is not a valid phone number')


class Contact(BaseModel):
    first_name = models.CharField(
        'Ad', 
        max_length=200,
        help_text='Kontentin uzunluğu maksimum 200-dür.'
    )
    last_name = models.CharField(
        'Soyad', 
        max_length=200,
        help_text='Kontentin uzunluğu maksimum 200-dür.'
    )
    email = models.EmailField(
        'E-poçt'
    )
    phone = models.CharField(
        'Telefon nömrəsi',
        max_length=17,
        help_text='Yalnız rəqəm daxil edin',
        validators=[validate_phone]
    )
    message = models.TextField(
        'Mesaj'
    )

    class Meta:
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Mesajlar'
        indexes = [models.Index(fields=['created_at'])]
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}-dən mesaj'