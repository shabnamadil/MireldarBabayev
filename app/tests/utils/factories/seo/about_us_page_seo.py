from apps.seo.models import AboutUsPageSeo

from .base_seo import BaseSeoFactory


class AboutUsPageSeoFactory(BaseSeoFactory):
    class Meta:
        model = AboutUsPageSeo
