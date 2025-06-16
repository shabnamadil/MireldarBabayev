from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.user.manager.custom_user_manager import CustomUserManager
from utils.models.base_model import BaseModel
from utils.validators.validate_image import (
    validate_image_content as ImageContentValidator,
)
from utils.validators.validate_image import (
    validate_image_extension as ImageExtensionValidator,
)
from utils.validators.validate_image import validate_image_size as ImageSizeValidator


class CustomUser(  # type: ignore[django-manager-missing]
    AbstractBaseUser, PermissionsMixin, BaseModel
):

    first_name = models.CharField(
        _("First Name"),
        max_length=30,
        help_text=_("The content length is a maximum of 30."),
    )
    last_name = models.CharField(
        _("Last Name"),
        max_length=30,
        help_text=_("The content length is a maximum of 30."),
    )
    email = models.EmailField(
        _("Email"),
        unique=True,
        error_messages={
            "unique": _("This email is already registered."),
            "invalid": _("Enter a valid email address."),
        },
    )
    image = models.ImageField(
        _("Image"),
        null=True,
        blank=True,
        upload_to="users/",
        validators=[
            ImageExtensionValidator,
            ImageSizeValidator,
            ImageContentValidator,
        ],
        help_text=_("Please upload a PNG or JPG file."),
    )

    # Required fields for AbstractBaseUser
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    @property
    def full_name(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return "Admin User"

    def __str__(self):
        return self.email
