from django.db import models
from django.core.exceptions import ValidationError

from utils.models.base_model import BaseModel
from ..models import Service

class Download(BaseModel):
    TYPE_CHOICES = (
        ('pdf', 'pdf'),
        ('docx', 'docx')
    )
    title = models.CharField(
        'Başlıq',
        max_length=200,
        help_text='Kontentin uzunluğu maksimum 200-dür.'
    )
    type = models.CharField(
        choices=TYPE_CHOICES,
        default='pdf',
        max_length=4
    )
    file = models.FileField(
        upload_to='services/downloads'
    )
    service  = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='downloads',
        null=True, blank=True
    )

    class Meta:
        verbose_name = ('Endirmə')
        verbose_name_plural = ('Endirmələr')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at'])
        ]

    def __str__(self) -> str:
        return self.title
    
    @property
    def file_size(self):
        if self.file and hasattr(self.file, 'size'):
            return self.file.size
        return 0  # Return 0 if there is no file

    @property
    def file_size_formatted(self):
        """Format the file size to a human-readable string (e.g., '2 MB', '512 KB')"""
        size = self.file_size
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} PB"