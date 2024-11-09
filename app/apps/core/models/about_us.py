from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from utils.models.base_model import BaseModel
from utils.models.singleton import SingletonModel


class AboutUs(BaseModel, SingletonModel):
    image = models.ImageField(
        'Foto',
        upload_to='about/',
        help_text='Haqqımızda səhifəsində göstərilməsi üçün foto yükləyin'
    )
    video_link = models.URLField(
        'Video linki',
        help_text='Haqqımızda səhifəsində göstərilməsi üçün video link'
    )
    content = RichTextUploadingField(
        'Haqqımızda məlumat',
        help_text='Haqqımızda səhifəsi üçün kontent'
    )
    mission = models.TextField(
        'Missiyamız',
    )
    vision = models.TextField(
        'Görüşümüz',
    )
    value = models.TextField(
        'Dəyərlərimiz',
    )
    
    class Meta:
        verbose_name = 'Haqqımızda'
        verbose_name_plural = 'Haqqımızda'
        indexes = [models.Index(fields=['created_at'])]
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'Haqqımızda məlumat'