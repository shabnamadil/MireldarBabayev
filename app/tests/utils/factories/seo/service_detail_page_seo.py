from apps.seo.models import ServiceDetailPageSeo

from .base_seo_detail import BaseSeoDetailFactory


class ServiceDetailPageSeoFactory(BaseSeoDetailFactory):
    class Meta:
        model = ServiceDetailPageSeo
