from apps.seo.models import BlogsPageSeo

from .base_seo import BaseSeoFactory


class BlogsPageSeoFactory(BaseSeoFactory):
    class Meta:
        model = BlogsPageSeo
