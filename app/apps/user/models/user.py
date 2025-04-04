from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.user.manager.custom_user_manager import CustomUserManager
from utils.models.base_model import BaseModel


class CustomUser(AbstractUser, BaseModel):
    first_name = models.CharField(
        max_length=30, help_text='Kontentin uzunluğu maksimum 30-dur.'
    )
    last_name = models.CharField(
        max_length=30, help_text='Kontentin uzunluğu maksimum 30-dur.'
    )
    email = models.EmailField(unique=True)
    image = models.ImageField(
        'Foto', null=True, blank=True, upload_to='users/'
    )

    objects = CustomUserManager()

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: list[str] = []

    class Meta:
        verbose_name = 'İstifadəçi'
        verbose_name_plural = 'İstifadəçilər'

    @property
    def full_name(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return 'Admin User'

    def __str__(self):
        return self.email
