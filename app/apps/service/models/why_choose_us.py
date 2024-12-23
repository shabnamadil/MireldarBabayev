from django.db import models
from django.core.exceptions import ValidationError

from utils.models.base_model import BaseModel


class WhyChooseUs(BaseModel):
    title = models.CharField(
        'Başlıq',
        max_length=200,
        unique=True,
        help_text='Kontentin uzunluğu maksimum 200-dür.'
    )
    short_description = models.TextField(
        'Qısa məlumat',
        unique=True
    )
    png = models.FileField(
        'PNG',
        upload_to='why_choose_us/'
    )

    class Meta:
        verbose_name = ('Nə üçün biz?')
        verbose_name_plural = ('Nə üçün biz?')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def clean(self) -> None:
        if self.png and not self.png.name.lower().endswith('.png'):
            raise ValidationError('Only PNG files are accepted.')
        super().clean()

    def __str__(self) -> str:
        return self.title