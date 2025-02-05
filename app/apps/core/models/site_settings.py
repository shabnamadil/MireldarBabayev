from django.db import models
from django.core.validators import MinLengthValidator

from utils.models.singleton import SingletonModel
from utils.helpers.validate_phone import PhoneValidationError
from utils.helpers.validate_work_hours import WorkHourValidationError


class SiteSettings(SingletonModel):
    site_name = models.CharField(
        max_length=100, 
        verbose_name="Site Name",
        validators=[MinLengthValidator(30)],
        help_text='Kontentin uzunluğu maksimum 100-dür.'
    )
    logo = models.ImageField(upload_to='logos/', verbose_name="Site Logo")
    favicon = models.ImageField(upload_to='favicons/', verbose_name="Favicon")
    location = models.CharField(
        'Məkan',
        max_length=100,
        help_text='Kontentin uzunluğu maksimum 100-dür.'
    )
    number = models.CharField(
        'Əlaqə nömrəsi',
        max_length=17,
        help_text='Yalnız rəqəm daxil edin. Məsələn: +994123456789',
        validators=[PhoneValidationError]
    )
    email = models.EmailField(
        'Email ünvanı'
    )
    work_hours = models.CharField(
        'İş saatları',
        max_length=13,
        validators=[WorkHourValidationError],
        help_text='Kontentin uzunluğu maksimum 13-dür. Nümunə: 09:00 - 18:00'
    )
    map_url = models.CharField(
        'Xəritə',
        max_length=500,
        help_text='Zəhmət olmasa, google məkanınızın "iframe" contentindən "src" attributunu daxil edin.'
    )
    facebook = models.URLField(
        'Facebook hesab linki',
        null=True, blank=True
    )
    youtube = models.URLField(
        'Youtube hesab linki',
        null=True, blank=True
    )
    instagram = models.URLField(
        'Instagram hesab linki',
        null=True, blank=True
    )
    twitter = models.URLField(
        'Twitter hesab linki',
        null=True, blank=True
    )
    linkedin = models.URLField(
        'Linkedin hesab linki',
        null=True, blank=True
    )
    tiktok = models.URLField(
        'Tiktok hesab linki',
        null=True, blank=True
    )
    footer_description = models.TextField(
        'Footer hissədə göstəriləcək mətn'
    )
    
    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name
