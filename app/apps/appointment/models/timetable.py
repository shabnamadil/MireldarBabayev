from django.db import models

from utils.models.base_model import BaseModel


class Timetable(BaseModel):
    start_time = models.DateTimeField('Görüşün başlama vaxtı', unique=True)
    end_time = models.DateTimeField('Görüşün bitmə vaxtı', unique=True)

    class Meta:
        verbose_name = 'Rezervasiya üçün uyğun vaxt'
        verbose_name_plural = 'Rezervasiya üçün uyğun vaxtlar'

    def __str__(self) -> str:
        return f"{
            self.start_time.strftime('%d %b %Y, %H:%M')} - {
            self.end_time.strftime('%d %b %Y, %H:%M')}"
