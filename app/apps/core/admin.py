from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import (
    Newsletter,
    Contact,
    Faq,
    SiteSettings,
    StatisticalIndicator,
    AboutUs,
    WhoWeAre,
    Testimoinal,
    Banner
)
from .forms import (
    ContactForm,
    SiteSettingsForm
)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_filter = ('created_at', )
    list_per_page = 20


@admin.register(Faq)
class FaqAdmin(TranslationAdmin):
    list_filter = ('created_at', )
    list_per_page = 20


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'created_date')
    list_filter = ('created_at', )
    date_hierarchy = 'created_at'
    list_per_page = 20
    search_fields = ('first_name', 'last_name', 'email', 'message', 'subject')
    form = ContactForm

    def full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'


class SingletonModelAdmin(TranslationAdmin):
    def has_add_permission(self, request):
        """Prevent adding more than one instance."""
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of the singleton instance."""
        return False


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin):
    list_display = ('site_name',)
    form = SiteSettingsForm


@admin.register(StatisticalIndicator)
class StatisticsAdmin(TranslationAdmin):
    list_display = ('name', 'value')
    list_filter = ('created_at', )
    list_per_page = 20
    date_hierarchy = 'created_at'
    search_fields = ('name', 'value')


@admin.register(AboutUs)
class AboutUsAdmin(TranslationAdmin):
    pass


@admin.register(WhoWeAre)
class WhoWeAreAdmin(TranslationAdmin):
    pass


@admin.register(Testimoinal)
class TestimonialAdmin(TranslationAdmin):
    pass

@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    pass