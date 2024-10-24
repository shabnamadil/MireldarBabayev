from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField

from utils.models.base_model import BaseModel
from utils.manager.published_blog import PublishedBlogManager
from .category import Category
from .ip import IP
from .tag import Tag

User = get_user_model()


class Blog(BaseModel):
        
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(
        'Məqalə başlığı', 
        max_length=100,
        unique=True
    )
    short_description = models.CharField(
        'Qısa məzmun',
        max_length=100
    )
    content = RichTextUploadingField(
        'Məqalə mətni'
    )
    image = models.ImageField(
        'Cover foto', 
        upload_to='blogs/'
    )
    category = models.ManyToManyField(
        Category, 
        related_name='blogs', 
        verbose_name='Kateqoriya'
    )
    tag = models.ManyToManyField(
        Tag,
        related_name='blogs',
        verbose_name='Teq',
        blank=True
    )
    slug=models.SlugField(
        'Link adı',
        null=True, blank=True,
        help_text="Bu qismi boş buraxın. Avtomatik doldurulacaq.",
        max_length=500    
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='blogs',
        verbose_name='Müəllif'
    )
    viewed_ips = models.ManyToManyField(
        IP, related_name="blogs", 
        verbose_name='Məqalənin görüntüləndiyi IP ünvanları',
        editable=False
    )
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.PUBLISHED
    )
    published_at = models.DateTimeField(
        'Paylaşım tarixi',
        null=True, blank=True
    )
    objects = models.Manager()
    published = PublishedBlogManager()

    class Meta:
        verbose_name = ('Məqalə')
        verbose_name_plural = ('Məqalələr')
        ordering = ['-published_at']
        indexes = [
            models.Index(fields=['-published_at'])
        ]
        
    @property
    def view_count(self):
        return self.viewed_ips.count() if self.viewed_ips else 0
    
    @property
    def published_date(self):
        local_published_time = timezone.localtime(self.published_at)
        return local_published_time.strftime('%d/%m/%Y, %H:%M')
    
    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        if self.status == self.Status.PUBLISHED and self.published_at is None:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)
    