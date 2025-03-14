import datetime

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from apps.blog.models import Blog, Comment
from apps.core.models import SiteSettings
from apps.seo.models import BlogDetailPageSeo
from apps.user.middleware import get_current_user

User = get_user_model()


@receiver(post_delete, sender=Comment)
def notify_user_on_comment_delete(sender, instance, **kwargs):
    current_user = get_current_user()
    if instance.author.is_staff or instance.author == current_user:
        return

    subject = "Your comment has been deleted"
    context = {
        'author_name': instance.author.get_full_name(),
        'blog_title': instance.blog.title,
        'comment_content': instance.content,
        'current_year': datetime.datetime.now().year,
        'settings': SiteSettings.objects.first(),
    }
    message = render_to_string(
        'components/email/blog/comment_author_send_email.html', context
    )
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
def create_blog_detail_page_object_seo(sender, instance, created, **kwargs):
    if created:
        BlogDetailPageSeo.objects.create(blog=instance)
