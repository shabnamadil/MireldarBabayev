from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from utils.models.singleton import SingletonModel


class WhoWeAre(SingletonModel):
    title = models.CharField(
        'Başlıq',
        max_length=50,
        help_text='Kontentin uzunluğu maksimum 50-dir.'
    )
    video_link = models.URLField(
        'Video linki',
        help_text='Biz kimik bölməsinsdə göstərilməsi üçün video link'
    )
    content = RichTextUploadingField(
        'Biz kimik',
        help_text='Biz kimik bölməsi üçün kontent'
    )
    
    class Meta:
        verbose_name = 'Biz kimik'
        verbose_name_plural = 'Biz kimik'
        indexes = [models.Index(fields=['created_at'])]
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'Biz kimik?'