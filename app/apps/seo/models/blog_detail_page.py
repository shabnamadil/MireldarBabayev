from django.db import models
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator
)

from utils.models.base_model import BaseModel
from apps.blog.models import Blog


class BlogDetailPageSeo(BaseModel):
    meta_description = models.TextField(
        validators=[
            MaxLengthValidator(160),
            MinLengthValidator(50)       
        ],
        help_text='Kontentin uzunluğu maksimum 50-160 aralığındadır.'
    )
    meta_keywords = models.TextField(
        validators=[
            MaxLengthValidator(160),
            MinLengthValidator(50)       
        ],
        help_text='Kontentin uzunluğu maksimum 50-160 aralığındadır.'
    )
    og_description = models.TextField(
        validators=[
            MaxLengthValidator(160),
            MinLengthValidator(50)       
        ],
        help_text='Kontentin uzunluğu maksimum 50-160 aralığındadır.'
    )
    blog = models.OneToOneField(
        Blog,
        related_name='detail_page_seo',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'SEO ==> {self.blog}'

    class Meta:
        verbose_name = 'Blog Detail Page SEO'
        verbose_name_plural = 'Blog Detail Page SEO'
