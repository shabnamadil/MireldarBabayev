from django.db import models
from utils.models.singleton import SingletonModel

class SiteSettings(SingletonModel):
    site_name = models.CharField(max_length=255, verbose_name="Site Name")
    logo = models.ImageField(upload_to='logos/', verbose_name="Site Logo")
    favicon = models.ImageField(upload_to='favicons/', verbose_name="Favicon")
    location = models.CharField(
        'Məkan',
        max_length=200
    )
    number = models.CharField(
        'Əlaqə nömrəsi',
        max_length=20
    )
    email = models.EmailField(
        'Email ünvanı'
    )
    work_hours = models.CharField(
        'İş saatları',
        max_length=200
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
