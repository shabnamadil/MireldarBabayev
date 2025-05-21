from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField
from utils.models.singleton import SingletonModel
from utils.validators.validate_social_media import (
    validate_youtube_video_id as VideoIdValidator,
)


class WhoWeAre(SingletonModel):
    title = models.CharField(
        _("Title"),
        max_length=50,
        help_text=_("The content length is a maximum of 50."),
    )
    video_link = models.CharField(
        _("Video ID"),
        help_text=_(
            'Example: From the link "https://www.youtube.com/watch?v=MKG_6BqnhpI", only "MKG_6BqnhpI" should be entered.'
        ),
        max_length=11,
        validators=[VideoIdValidator],
    )
    content = RichTextUploadingField(
        _("Content"), help_text=_("Content for the Who We Are section.")
    )

    class Meta:
        verbose_name = _("Who We Are")
        verbose_name_plural = _("Who We Are")

    def __str__(self) -> str:
        return str(_("Biz kimik?"))
