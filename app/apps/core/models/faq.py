from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel


class Faq(BaseModel):
    question = models.TextField(_("Question"))
    response = models.TextField(_("Response"))

    class Meta:
        verbose_name = _("Faq")
        verbose_name_plural = _("Faqs")
        constraints = [
            UniqueConstraint(
                fields=["question", "response"],
                name="unique_faq_question_response",
            )
        ]

    def __str__(self) -> str:
        return self.question
