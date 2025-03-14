from django.db import models
from django.db.models import UniqueConstraint

from utils.models.base_model import BaseModel


class Faq(BaseModel):
    question = models.TextField('Sual')
    response = models.TextField('Cavab')

    class Meta:
        verbose_name = 'Tez-tez verilən sual'
        verbose_name_plural = 'Tez-tez verilən suallar'
        constraints = [
            UniqueConstraint(
                fields=['question', 'response'],
                name='unique_faq_question_response',
            )
        ]

    def __str__(self) -> str:
        return self.question
