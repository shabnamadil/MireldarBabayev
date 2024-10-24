from django.db import models

from utils.models.base_model import BaseModel


class Category(BaseModel):
    name = models.CharField(
        'Kateqoriya adı', 
        max_length=150,
        unique=True
    )

    class Meta:
        verbose_name = ('Məqalə kateqoriyası')
        verbose_name_plural = ('Məqalə kateqoriyaları')

    def __str__(self) -> str:
        return self.name