from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.blog.models import Blog
from utils.models.base_seo_detail import BaseSeoDetailModel


class BlogDetailPageSeo(BaseSeoDetailModel):
    blog = models.OneToOneField(
        Blog,
        related_name="detail_page_seo",
        on_delete=models.CASCADE,
        verbose_name=_("Blog"),
    )

    class Meta:
        verbose_name = _("BlogDetailPageSeo")
        verbose_name_plural = _("BlogDetailPageSeos")
