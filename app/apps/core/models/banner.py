from django.db import models
from django.core.exceptions import ValidationError


from utils.models.base_model import BaseModel


class Banner(BaseModel):
    title = models.CharField(
        'Başlıq', 
        max_length=200
    )
    subtitle = models.CharField(
        'Alt başlıq', 
        max_length=100
    )
    description = models.TextField(
        'Qısa izah'
    )
    png = models.ImageField(
        'Banner foto',
        upload_to='banner',
        help_text='PNG formatda daxil edin. Ölçü: 720x726px'
    )
    video_id= models.CharField(
        'Video link id',
        help_text='Nümunə: "https://www.youtube.com/watch?v=MKG_6BqnhpI" linkindən  "MKG_6BqnhpI" daxil edilməlidir',
        max_length=11
    )


    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Bannerlər'
        indexes = [models.Index(fields=['created_at'])]
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.title
    

    def clean(self) -> None:
        if self.png and not self.png.name.lower().endswith('.png'):
            raise ValidationError('Only PNG files are accepted.')
        super().clean()