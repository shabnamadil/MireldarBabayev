from django.db import models

from utils.models.base_model import BaseModel


class Contact(BaseModel):
    first_name = models.CharField(
        'Ad', 
        max_length=200
    )
    last_name = models.CharField(
        'Soyad', 
        max_length=200
    )
    email = models.EmailField(
        'E-poçt'
    )
    phone = models.CharField(
        'Telefon nömrəsi',
        max_length=20,
        help_text='Yalnız rəqəm daxil edin'
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