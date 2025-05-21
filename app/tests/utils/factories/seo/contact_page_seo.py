from apps.seo.models import ContactPageSeo

from .base_seo import BaseSeoFactory


class ContactPageSeoFactory(BaseSeoFactory):
    class Meta:
        model = ContactPageSeo
