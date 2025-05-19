from django.utils.translation import gettext_lazy as _

from utils.models.base_seo_model import BaseSeoModel


class ContactPageSeo(BaseSeoModel):
    class Meta:
        verbose_name = _('ContactPageSeo')
        verbose_name_plural = _('ContactPageSeos')
