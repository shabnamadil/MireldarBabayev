from django.utils.translation import gettext_lazy as _

from utils.models.base_seo_model import BaseSeoModel


class AppointmentPageSeo(BaseSeoModel):

    class Meta:
        verbose_name = _('AppointmentPageSeo')
        verbose_name_plural = _('AppointmentPageSeos')
