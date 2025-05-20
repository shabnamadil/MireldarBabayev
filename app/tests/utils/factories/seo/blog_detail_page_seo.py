from apps.seo.models import BlogDetailPageSeo

from .base_seo_detail import BaseSeoDetailFactory


class BlogDetailPageSeoFactory(BaseSeoDetailFactory):
    class Meta:
        model = BlogDetailPageSeo
