from apps.seo.models import FaqPageSeo

from .base_seo import BaseSeoFactory


class FaqPageSeoFactory(BaseSeoFactory):
    class Meta:
        model = FaqPageSeo
