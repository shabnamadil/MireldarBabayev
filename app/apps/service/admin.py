from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import (
    Service,
    Download,
    WhyChooseUs,
    Coworker
)
from .forms import DownloadBaseForm


class MediaAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Service)
class ServiceAdmin(MediaAdmin):
    list_filter = ('created_at', )
    readonly_fields = ('slug', )


@admin.register(Download)
class DownloadAdmin(MediaAdmin):
    list_display = ('title', 'type', 'get_file_size')
    list_filter = ('created_at', 'type')
    form = DownloadBaseForm

    def get_file_size(self, obj):
        return obj.file_size_formatted
    get_file_size.short_description = 'File size'


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(MediaAdmin):
    pass


@admin.register(Coworker)
class CoworkerAdmin(MediaAdmin):
    pass