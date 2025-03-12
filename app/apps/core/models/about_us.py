from django.db import models

from ckeditor_uploader.fields import (
    RichTextUploadingField,
)
from utils.models.singleton import SingletonModel


class AboutUs(SingletonModel):
    image = models.ImageField(
        "Foto",
        upload_to="about/",
        help_text="Haqqımızda səhifəsində göstərilməsi üçün foto yükləyin",
    )
    video_id = models.CharField(
        "Video link id",
        help_text='Nümunə: "https://www.youtube.com/watch?v=MKG_6BqnhpI" linkindən  "MKG_6BqnhpI" daxil edilməlidir',
        max_length=11,
    )
    content = RichTextUploadingField(
        "Haqqımızda məlumat",
        help_text="Haqqımızda səhifəsi üçün kontent",
    )
    mission = models.TextField(
        "Missiyamız",
    )
    vision = models.TextField(
        "Görüşümüz",
    )
    value = models.TextField(
        "Dəyərlərimiz",
    )

    class Meta:
        verbose_name = "Haqqımızda"
        verbose_name_plural = "Haqqımızda"

    def __str__(self) -> str:
        return f"Haqqımızda məlumat"
