from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.seo.models import ServiceDetailPageSeo

from .models import Service


@receiver(post_save, sender=Service)
def create_service_object_seo(sender, instance, created, **kwargs):
    if created:
        ServiceDetailPageSeo.objects.create(service=instance)
