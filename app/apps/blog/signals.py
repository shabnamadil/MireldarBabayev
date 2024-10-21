from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from apps.blog.models import Blog


@receiver(post_save, sender=Blog)
def define_published_date(sender, instance, created, *args, **kwargs):
    if created:    
        if instance.status == instance.Status.PUBLISHED:
            print(instance.status)
            print('yes')
            instance.published_at = timezone.now()
            instance.save()