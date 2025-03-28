from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

from apps.service.models import Service
from utils.models.base_model import BaseModel


class ServiceDetailPageSeo(BaseModel):
    meta_description = models.TextField(
        validators=[MaxLengthValidator(160), MinLengthValidator(50)],
        help_text='Kontentin uzunluğu maksimum 50-160 aralığındadır.',
    )
    meta_keywords = models.TextField(
        validators=[MaxLengthValidator(160), MinLengthValidator(50)],
        help_text='Kontentin uzunluğu maksimum 50-160 aralığındadır.',
    )
    og_description = models.TextField(
        validators=[MaxLengthValidator(160), MinLengthValidator(50)],
        help_text='Kontentin uzunluğu maksimum 50-160 aralığındadır.',
    )
    service = models.OneToOneField(
        Service, related_name='detail_page_seo', on_delete=models.CASCADE
    )

    def __str__(self):
        return f'SEO ==> {self.service}'

    class Meta:
        verbose_name = 'Service Detail Page SEO'
        verbose_name_plural = 'Service Detail Page SEO'
