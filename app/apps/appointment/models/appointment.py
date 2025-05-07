from django.db import models

from utils.models.base_model import BaseModel
from utils.validators.validate_phone import validate_phone_value

from .timetable import Timetable


class Appointment(BaseModel):
    full_name = models.CharField(
        'Ad, Soyad',
        max_length=100,
        help_text='Kontentin uzunluğu maksimum 100-dür.',
    )
    phone = models.CharField(
        'Əlaqə nömrəsi',
        max_length=17,
        validators=[validate_phone_value],
        help_text='Yalnız rəqəm daxil edin',
    )
    location = models.CharField('Məkan', max_length=200, null=True, blank=True)
    message = models.TextField('Mesaj', null=True, blank=True)
    available_time = models.OneToOneField(
        Timetable,
        verbose_name='Uyğun tarix',
        related_name='appointment',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Rezervasiya'
        verbose_name_plural = 'Rezervasiyalar'
        indexes = [models.Index(fields=['created_at'])]
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.full_name} - {self.available_time}'
