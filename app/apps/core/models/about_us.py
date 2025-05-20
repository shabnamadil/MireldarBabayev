from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField
from utils.models.singleton import SingletonModel
from utils.validators.validate_image import (
    validate_image_content as ImageContentValidator,
)
from utils.validators.validate_image import (
    validate_image_extension as ImageExtensionValidator,
)
from utils.validators.validate_image import validate_image_size as ImageSizeValidator
from utils.validators.validate_social_media import (
    validate_youtube_video_id as VideoIdValidator,
)


class AboutUs(SingletonModel):
    image = models.ImageField(
        _("Image"),
        upload_to="about/",
        validators=[
            ImageSizeValidator,
            ImageContentValidator,
            ImageExtensionValidator,
        ],
        help_text=_(
            "Kindly upload a photo for the About page. Image size shoud not exceed 2mb."
        ),
    )
    video_id = models.CharField(
        _("Video ID"),
        help_text=_(
            'Example: From the link "https://www.youtube.com/watch?v=MKG_6BqnhpI", only "MKG_6BqnhpI" should be entered.'
        ),
        max_length=11,
        validators=[VideoIdValidator],
    )
    content = RichTextUploadingField(_("About Us"), help_text=_("About Us content"))
    mission = models.TextField(
        _("Mission"),
    )
    vision = models.TextField(
        _("Vision"),
    )
    value = models.TextField(
        _("Values"),
    )

    class Meta:
        verbose_name = _("About Us")
        verbose_name_plural = _("About Us")

    def __str__(self) -> str:
        return str(_("About Us Information"))
