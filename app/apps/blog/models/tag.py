from django.db import models
from django.utils.text import slugify

from utils.models.base_model import BaseModel


class Tag(BaseModel):
    name = models.CharField(
        'Tag', 
        max_length=150,
        unique=True
    )
    slug=models.SlugField(
        'Link adı',
        null=True, blank=True,
        help_text="Bu qismi boş buraxın. Avtomatik doldurulacaq.",
        max_length=500    
    )

    class Meta:
        verbose_name = ('Məqalə teqi')
        verbose_name_plural = ('Məqalə teqləri')

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args, **kwargs)