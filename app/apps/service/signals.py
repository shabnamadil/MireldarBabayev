from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Service
from apps.seo.models import ServiceDetailPageSeo


@receiver(post_save, sender=Service)
def create_service_object_seo(sender, instance, created, **kwargs):
    if created:
        ServiceDetailPageSeo.objects.create(service=instance)