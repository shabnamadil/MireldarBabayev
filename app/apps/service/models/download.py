import os

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.service.models.service import Service
from utils.models.base_model import BaseModel
from utils.validators.validate_file import (
    validate_extension,
    validate_file_content,
    validate_type,
)


class Download(BaseModel):

    TYPE_CHOICES = (("pdf", "pdf"), ("docx", "docx"))

    title = models.CharField(
        _("Title"),
        help_text=_("Leave it blank. It will be filled automatically."),
        null=True,
        blank=True,
        editable=False,
    )
    type = models.CharField(
        _("File type"), choices=TYPE_CHOICES, default="pdf", max_length=4
    )
    file = models.FileField(_("File"), upload_to="services/downloads")
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="downloads",
        null=True,
        blank=True,
        verbose_name=_("Service"),
    )

    class Meta:
        verbose_name = _("Download")
        verbose_name_plural = _("Downloads")
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["-created_at"])]
        unique_together = ("service", "title")

    def __str__(self):
        return self.title

    @property
    def file_size(self):
        if self.file and hasattr(self.file, "size"):
            return self.file.size
        return 0  # Return 0 if there is no file

    @property
    def file_size_formatted(self):
        """Format the file size to a human-readable string (e.g., '2 MB', '512 KB')"""
        size = self.file_size
        for unit in ["B", "KB", "MB", "GB", "TB"]:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} PB"

    def clean(self):
        cd = super().clean()
        if self.file:
            validate_extension(self.file.name)
            validate_type(self.file.name, self.type)
            validate_file_content(self.file, self.type)
        return cd

    def save(self, *args, **kwargs):
        if self.file:
            base_name = os.path.splitext(os.path.basename(self.file.name))[0]
            self.title = base_name
        super().save(*args, **kwargs)
