from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

import datetime

from apps.blog.models import (
    Comment, 
    Blog
)
from apps.core.models import SiteSettings
from apps.seo.models import BlogDetailPageSeo

User = get_user_model()

@receiver(post_delete, sender=Comment)
def notify_user_on_comment_delete(sender, instance, **kwargs):
    if instance.author.is_staff:
        return

    subject = "Your comment has been deleted"
    context = {
        'author_name' : instance.author.get_full_name(),
        'blog_title' : instance.blog.title,
        'comment_content' : instance.content,
        'current_year' : datetime.datetime.now().year,
        'settings' : SiteSettings.objects.first()
    }
    message = render_to_string('components/email/blog/comment_author_send_email.html', context)
    recipient_list = [instance.author.email]
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False,
        html_message=message,
    )


@receiver(post_save, sender=Blog)
def create_service_object_seo(sender, instance, created, **kwargs):
    if created:
        BlogDetailPageSeo.objects.create(blog=instance)