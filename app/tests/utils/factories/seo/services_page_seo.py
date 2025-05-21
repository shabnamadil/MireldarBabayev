from apps.seo.models import ServicesPageSeo

from .base_seo import BaseSeoFactory


class ServicesPageSeoFactory(BaseSeoFactory):
    class Meta:
        model = ServicesPageSeo
