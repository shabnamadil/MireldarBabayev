from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
)
from django.db import models

from utils.models.singleton import SingletonModel


class FaqPageSeo(SingletonModel):
    meta_title = models.CharField(
        max_length=60,
        validators=[MinLengthValidator(30)],
        help_text="Kontentin uzunluğu maksimum 30-60 aralığındadır.",
    )
    meta_description = models.TextField(
        validators=[
            MaxLengthValidator(160),
            MinLengthValidator(50),
        ],
        help_text="Kontentin uzunluğu maksimum 50-160 aralığındadır.",
    )
    meta_keywords = models.TextField(
        validators=[
            MaxLengthValidator(160),
            MinLengthValidator(50),
        ],
        help_text="Kontentin uzunluğu maksimum 50-160 aralığındadır.",
    )
    og_title = models.CharField(
        max_length=60,
        validators=[MinLengthValidator(30)],
        help_text="Kontentin uzunluğu maksimum 30-60 aralığındadır.",
    )
    og_description = models.TextField(
        validators=[
            MaxLengthValidator(160),
            MinLengthValidator(50),
        ],
        help_text="Kontentin uzunluğu maksimum 50-160 aralığındadır.",
    )
    og_image = models.ImageField(upload_to="seo-images/faq/")

    def __str__(self):
        return self.meta_title

    class Meta:
        verbose_name = "Faq Page SEO"
        verbose_name_plural = "Faq Page SEO"
