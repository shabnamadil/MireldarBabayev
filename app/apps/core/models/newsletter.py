from django.db import models

from utils.models.base_model import BaseModel


class Newsletter(BaseModel):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Abunə'
        verbose_name_plural = 'Abunələr'

    def __str__(self) -> str:
        return self.email
