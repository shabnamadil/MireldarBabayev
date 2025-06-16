from django.utils.translation import gettext_lazy as _

from utils.models.base_seo_model import BaseSeoModel


class FaqPageSeo(BaseSeoModel):

    class Meta:
        verbose_name = _("FaqPageSeo")
        verbose_name_plural = _("FaqPageSeos")
