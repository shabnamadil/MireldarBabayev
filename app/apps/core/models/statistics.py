from django.core.exceptions import ValidationError
from django.db import models

from utils.models.base_model import BaseModel


class StatisticalIndicator(BaseModel):
    png = models.FileField(
        'png', upload_to='statistics/', help_text='PNG formatda daxil edin'
    )
    value = models.IntegerField(
        'Statistik göstəricinin dəyəri',
    )
    name = models.CharField(
        'Statistik göstəricinin adı',
        max_length=50,
        unique=True,
        help_text='Kontentin uzunluğu maksimum 50-dir.',
    )

    class Meta:
        verbose_name = 'Statistika'
        verbose_name_plural = 'Statistikalar'
        indexes = [models.Index(fields=['created_at'])]
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.name

    def clean(self) -> None:
        if self.png and not self.png.name.lower().endswith('.png'):
            raise ValidationError('Only PNG files are accepted.')
        super().clean()
