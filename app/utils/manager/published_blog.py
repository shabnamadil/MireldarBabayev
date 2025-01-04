from django.db import models
from apps.blog import models as mod


class PublishedBlogManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=mod.Blog.Status.PUBLISHED)