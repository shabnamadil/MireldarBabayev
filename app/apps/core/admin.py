from django.contrib import admin

from modeltranslation.admin import (
    TranslationAdmin,
)

from .forms import SiteSettingsForm
from .models import (
    AboutUs,
    Banner,
    Contact,
    Faq,
    Newsletter,
    SiteSettings,
    StatisticalIndicator,
    Testimoinal,
    WhoWeAre,
)


class MediaAdmin(TranslationAdmin):
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_filter = ("created_at",)
    list_per_page = 20


@admin.register(Faq)
class FaqAdmin(MediaAdmin):
    list_filter = ("created_at",)
    list_per_page = 20


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "phone",
        "created_date",
    )
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
    list_per_page = 20
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "message",
        "subject",
    )

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class SingletonModelAdmin(TranslationAdmin):
    def has_add_permission(self, request):
        """Prevent adding more than one instance."""
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of the singleton instance."""
        return False

    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin):
    list_display = ("site_name",)
    form = SiteSettingsForm


@admin.register(StatisticalIndicator)
class StatisticsAdmin(MediaAdmin):
    list_display = ("name", "value")
    list_filter = ("created_at",)
    list_per_page = 20
    date_hierarchy = "created_at"
    search_fields = ("name", "value")


@admin.register(AboutUs)
class AboutUsAdmin(SingletonModelAdmin):
    pass


@admin.register(WhoWeAre)
class WhoWeAreAdmin(SingletonModelAdmin):
    pass


@admin.register(Testimoinal)
class TestimonialAdmin(MediaAdmin):
    pass


@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    pass
