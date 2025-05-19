from django.utils.translation import gettext_lazy as _

from utils.models.base_seo_model import BaseSeoModel


class AboutUsPageSeo(BaseSeoModel):
    class Meta:
        verbose_name = _('AboutUsPageSeo')
        verbose_name_plural = _('AboutUsPageSeos')
