from django.db import models
from django.core.exceptions import ValidationError

from utils.models.base_model import BaseModel


class Coworker(BaseModel):
    name = models.CharField(
        'Əməkdaş şirkətin adı',
        max_length=200,
        help_text='Kontentin uzunluğu maksimum 200-dür.'
    )
    png = models.FileField(
        'Logo',
        upload_to='coworkers/',
        help_text='PNG formatda daxil edin.'
    )

    class Meta:
        verbose_name = ('Əməkdaş')
        verbose_name_plural = ('Əməkdaşlar')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def __str__(self) -> str:
        return self.name
    
    def clean(self) -> None:
        if self.png and not self.png.name.lower().endswith('.png'):
            raise ValidationError('Only PNG files are accepted.')
        super().clean()