from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField
from utils.manager.published_blog import PublishedBlogManager
from utils.models.base_model import BaseModel
from utils.validators.validate_image import (
    validate_image_content as ImageContentValidator,
)
from utils.validators.validate_image import (
    validate_image_extension as ImageExtensionValidator,
)
from utils.validators.validate_image import validate_image_size as ImageSizeValidator

from .category import Category
from .ip import IP
from .tag import Tag

User = get_user_model()


class Blog(BaseModel):

    class Status(models.TextChoices):
        DRAFT = "DF", _("Draft")
        PUBLISHED = "PB", _("Published")

    title = models.CharField(
        _("Title"),
        max_length=100,
        unique=True,
        help_text=_("The content length is a maximum of 100."),
    )
    short_description = models.CharField(
        _("Short description"),
        max_length=200,
        help_text=_("The content length is a maximum of 200."),
    )
    content = RichTextUploadingField(_("Article content"))
    image = models.ImageField(
        _("Cover photo"),
        upload_to="blogs/",
        validators=[
            ImageSizeValidator,
            ImageContentValidator,
            ImageExtensionValidator,
        ],
        help_text=_("Image size shoud not exceed 2mb."),
    )
    category = models.ManyToManyField(
        Category, related_name="blogs", verbose_name=_("Category")
    )
    tag: models.ManyToManyField = models.ManyToManyField(
        Tag, related_name="blogs", verbose_name=_("Tag"), blank=True
    )
    slug = models.SlugField(
        _("Slug"),
        null=True,
        blank=True,
        help_text=_("Leave it blank. This field will be filled automatically."),
        max_length=500,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blogs",
        verbose_name=_("Author"),
    )
    viewed_ips: models.ManyToManyField = models.ManyToManyField(
        IP,
        related_name="blogs",
        verbose_name=_("Viewed IP addresses"),
        editable=False,
    )
    view_count = models.IntegerField(_("View count"), default=0, editable=False)
    status = models.CharField(
        _("Status"), max_length=2, choices=Status.choices, default=Status.PUBLISHED
    )
    published_at = models.DateTimeField(_("Published date"), null=True, blank=True)
    objects: models.Manager["Blog"] = models.Manager()
    published: PublishedBlogManager = PublishedBlogManager()

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
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
        if self.pk and not self.category.exists():
            raise ValidationError({"category": _("At least one category is required.")})
        return cd

    def __str__(self) -> str:
        return self.title
