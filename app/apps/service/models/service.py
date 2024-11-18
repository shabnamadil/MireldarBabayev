from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.urls import reverse_lazy

from ckeditor_uploader.fields import RichTextUploadingField

from utils.models.base_model import BaseModel


class Service(BaseModel):
    COLOR_CHOICES = (
        ('yellow', 'yellow'),
        ('green', 'green'),
        ('blue', 'blue')
    )
    name = models.CharField(
        'Servisin adı',
        max_length=200,
        unique=True
    )
    short_description = models.TextField(
        'Qısa məlumat'
    )
    png = models.FileField(
        'PNG',
        upload_to='services/',
        help_text='PNG formatda daxil edin. Ölçü: 94x74px'
    )
    image = models.ImageField(
        'Əsas foto',
        upload_to='services/images/'
    )
    title = models.CharField(
        'Başlıq',
        unique=True,
        max_length=250
    )
    content = RichTextUploadingField(
        'Servis haqqında geniş məlumat'
    )
    background_color = models.CharField(
        choices=COLOR_CHOICES,
        default = 'blue',
        max_length=20
    )
    slug=models.SlugField(
        'Link adı',
        null=True, blank=True,
        help_text="Bu qismi boş buraxın. Avtomatik doldurulacaq.",
        max_length=500    
    )

    class Meta:
        verbose_name = ('Xidmət')
        verbose_name_plural = ('Xidmətlər')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def clean(self) -> None:
        if self.png and not self.png.name.lower().endswith('.png'):
            raise ValidationError('Only PNG files are accepted.')
        super().clean()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('service-detail', args=[self.slug])

    def __str__(self) -> str:
        return self.name
    