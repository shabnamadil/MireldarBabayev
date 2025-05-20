from apps.seo.models import HomePageSeo

from .base_seo import BaseSeoFactory


class HomePageSeoFactory(BaseSeoFactory):
    class Meta:
        model = HomePageSeo
