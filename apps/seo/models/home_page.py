from django.db import models
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator
)

from utils.models.singleton import SingletonModel


class HomePageSeo(SingletonModel):
    meta_title = models.CharField(
        max_length=60,
        validators=[MinLengthValidator(30)]
    )
    meta_description = models.TextField(
        validators=[
        MaxLengthValidator(160),
        MinLengthValidator(50)]
    )
    meta_keywords = models.TextField(
        validators=[
            MaxLengthValidator(160),
            MinLengthValidator(50)       
        ]
    )
    og_title = models.CharField(
        max_length=60,
        validators=[
            MinLengthValidator(30)
        ]
    )
    og_description = models.TextField(
        validators=[
        MaxLengthValidator(160),
        MinLengthValidator(50)]
    )
    og_image = models.ImageField(upload_to='seo-images/home/')

    def __str__(self):
        return self.meta_title

    class Meta:
        verbose_name = 'Homepage SEO'
        verbose_name_plural = 'Homepage SEO'