from django.utils.translation import gettext_lazy as _

from utils.models.base_seo_model import BaseSeoModel


class BlogsPageSeo(BaseSeoModel):
    class Meta:
        verbose_name = _("BlogsPageSeo")
        verbose_name_plural = _("BlogsPageSeos")
