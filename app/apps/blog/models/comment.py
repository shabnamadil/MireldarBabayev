from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models.base_model import BaseModel

from .blog import Blog

User = get_user_model()


class Comment(BaseModel):
    content = models.TextField(_("Comment content"))
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Blog"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Comment author"),
    )

    class Meta:
        verbose_name = _("Article comment")
        verbose_name_plural = _("Article comments")
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["-created_at"])]

    @property
    def truncated_comment(self):
        max_words = 3
        words = self.content.split()
        truncated_words = words[:max_words]
        truncated_content = " ".join(truncated_words)

        if len(words) > max_words:
            truncated_content += " ..."

        return truncated_content

    def __str__(self):
        return self.truncated_comment
