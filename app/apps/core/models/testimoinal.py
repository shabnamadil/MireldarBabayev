from django.core.validators import (
    MaxLengthValidator,
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
)
from django.db import models

from utils.models.base_model import BaseModel


class Testimoinal(BaseModel):
    client_image = models.ImageField(
        "Müştəri fotosu",
        upload_to="testimonials/",
        help_text="Foto '170x170px' ölçüsündə olmalıdır. ",
    )
    client_full_name = models.CharField(
        "Müştərinin ad, soyadı",
        max_length=20,
        help_text="Kontentin uzunluğu maksimum 20-dir.",
    )
    client_profession = models.CharField(
        "Müştərinin peşəsi",
        max_length=100,
        help_text="Kontentin uzunluğu maksimum 200-dür.",
    )
    client_comment = models.TextField(
        "Müştəri rəyi",
        validators=[MinLengthValidator(150), MaxLengthValidator(155)],
    )
    star = models.IntegerField(
        "Müştərinin verdiyi qiymət",
        help_text="5 ballıq sistem üzərindən dəyərləndirmə",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    class Meta:
        verbose_name = "Müştəri rəyi"
        verbose_name_plural = "Müştəri rəyləri"
        indexes = [models.Index(fields=["created_at"])]
        ordering = ("-created_at",)

    @property
    def star_range(self):
        return range(self.star)

    def __str__(self) -> str:
        return f"{self.client_full_name}-in rəyi"
