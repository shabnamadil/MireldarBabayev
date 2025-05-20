from apps.seo.models import AppointmentPageSeo

from .base_seo import BaseSeoFactory


class AppointmentPageSeoFactory(BaseSeoFactory):
    class Meta:
        model = AppointmentPageSeo
