from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.service.models import Service
from utils.models.base_seo_detail import BaseSeoDetailModel


class ServiceDetailPageSeo(BaseSeoDetailModel):
    service = models.OneToOneField(
        Service,
        related_name='detail_page_seo',
        on_delete=models.CASCADE,
        verbose_name=_('Service'),
    )

    class Meta:
        verbose_name = _('ServiceDetailPageSeo')
        verbose_name_plural = _('ServiceDetailPageSeos')

    def __str__(self):
        return f'SEO ==> {self.service}'
