from django.db import models

from utils.models.base_model import BaseModel


class Tag(BaseModel):
    name = models.CharField(
        'Tag', 
        max_length=150,
        unique=True
    )

    class Meta:
        verbose_name = ('Məqalə teqi')
        verbose_name_plural = ('Məqalə teqləri')

    def __str__(self) -> str:
        return self.name