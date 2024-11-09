from django.contrib import admin

from .models import (
    Service,
    Download,
    WhyChooseUs,
    Coworker
)
from .forms import DownloadBaseForm


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_filter = ('created_at', )
    readonly_fields = ('slug', )


@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'get_file_size')
    list_filter = ('created_at', 'type')
    form = DownloadBaseForm

    def get_file_size(self, obj):
        return obj.file_size_formatted
    get_file_size.short_description = 'File size'


admin.site.register(WhyChooseUs)
admin.site.register(Coworker)