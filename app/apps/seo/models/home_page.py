from django.utils.translation import gettext_lazy as _

from utils.models.base_seo_model import BaseSeoModel


class HomePageSeo(BaseSeoModel):
    class Meta:
        verbose_name = _('HomePageSeo')
        verbose_name_plural = _('HomePageSeos')
