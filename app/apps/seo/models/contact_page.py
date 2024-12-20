from django.db import models
from django.core.validators import MaxLengthValidator

from utils.models.singleton import SingletonModel


class ContactPageSeo(SingletonModel):
    meta_title = models.CharField(max_length=60)
    meta_description = models.TextField(validators=[MaxLengthValidator(160)])
    meta_keywords = models.TextField()
    og_title = models.CharField(max_length=60)
    og_description = models.TextField(validators=[MaxLengthValidator(160)])
    og_image = models.ImageField(upload_to='seo-images/contact/')

    def __str__(self):
        return self.meta_title

    class Meta:
        verbose_name = 'Contact Page SEO'
        verbose_name_plural = 'Contact Page SEO'
