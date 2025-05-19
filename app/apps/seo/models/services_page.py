from django.utils.translation import gettext_lazy as _

from utils.models.base_seo_model import BaseSeoModel


class ServicesPageSeo(BaseSeoModel):

    class Meta:
        verbose_name = _('ServicesPageSeo')
        verbose_name_plural = _('ServicesPageSeos')
