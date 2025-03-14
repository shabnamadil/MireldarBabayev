from django.db import models

from utils.helpers.slugify import custom_slugify
from utils.models.base_model import BaseModel


class Category(BaseModel):
    name = models.CharField(
        'Kateqoriya adı',
        max_length=150,
        unique=True,
        help_text='Kontentin uzunluğu maksimum 150-dir.',
    )
    slug = models.SlugField(
        'Link adı',
        null=True,
        blank=True,
        help_text="Bu qismi boş buraxın. Avtomatik doldurulacaq.",
        max_length=500,
    )

    class Meta:
        verbose_name = 'Məqalə kateqoriyası'
        verbose_name_plural = 'Məqalə kateqoriyaları'

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = custom_slugify(self.name)
        super().save(*args, **kwargs)
