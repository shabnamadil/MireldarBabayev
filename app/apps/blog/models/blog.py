from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField
from utils.manager.published_blog import PublishedBlogManager
from utils.models.base_model import BaseModel

from .category import Category
from .ip import IP
from .tag import Tag

User = get_user_model()


class Blog(BaseModel):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(
        "Məqalə başlığı",
        max_length=100,
        unique=True,
        help_text="Kontentin uzunluğu maksimum 100-dür.",
    )
    short_description = models.CharField(
        "Qısa məzmun",
        max_length=200,
        help_text="Kontentin uzunluğu maksimum 200-dür.",
    )
    content = RichTextUploadingField("Məqalə mətni")
    image = models.ImageField("Cover foto", upload_to="blogs/")
    category = models.ManyToManyField(
        Category, related_name="blogs", verbose_name="Kateqoriya"
    )
    tag: models.ManyToManyField = models.ManyToManyField(
        Tag, related_name="blogs", verbose_name="Teq", blank=True
    )
    slug = models.SlugField(
        "Link adı",
        null=True,
        blank=True,
        help_text="Bu qismi boş buraxın. Avtomatik doldurulacaq.",
        max_length=500,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blogs",
        verbose_name="Müəllif",
    )
    viewed_ips: models.ManyToManyField = models.ManyToManyField(
        IP,
        related_name="blogs",
        verbose_name="Məqalənin görüntüləndiyi IP ünvanları",
        editable=False,
    )
    view_count = models.IntegerField(default=0, editable=False)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.PUBLISHED
    )
    published_at = models.DateTimeField("Paylaşım tarixi", null=True, blank=True)
    objects: models.Manager["Blog"] = models.Manager()
    published: PublishedBlogManager = PublishedBlogManager()

    class Meta:
        verbose_name = "Məqalə"
        verbose_name_plural = "Məqalələr"
        ordering = ["-published_at"]
        indexes = [models.Index(fields=["-published_at"])]

    def increment_view_count(self, ip_instance: IP) -> None:
        if not self.viewed_ips.filter(id=ip_instance.id).exists():
            self.viewed_ips.add(ip_instance)
            self.view_count += 1
            self.save()

    @property
    def published_date(self) -> str:
        local_published_time = timezone.localtime(self.published_at)
        return local_published_time.strftime("%d %b, %Y")

    @property
    def sitemap_image(self) -> str | None:
        return self.image.url if self.image else None

    def get_absolute_url(self):
        return reverse_lazy("blog-detail", args=[self.slug])

    def clean(self):
        cd = super().clean()
        if Blog.objects.exclude(pk=self.pk).filter(title=self.title).exists():
            raise ValidationError(_(f'"{self.title}" article already exists.'))
        return cd

    def __str__(self) -> str:
        return self.title
