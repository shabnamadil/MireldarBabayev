from django.db import models

from utils.models.base_model import BaseModel


class Faq(BaseModel):
    question = models.TextField(
        'Sual',
        unique=True
    )
    response = models.TextField(
        'Cavab'
    )
    
    class Meta:
        verbose_name = 'Tez-tez verilən sual'
        verbose_name_plural = 'Tez-tez verilən suallar'

    def __str__(self) -> str:
        return self.question