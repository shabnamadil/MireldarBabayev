from django.contrib import admin

from modeltranslation.admin import (
    TranslationAdmin,
)

from .models import (
    AboutUsPageSeo,
    AppointmentPageSeo,
    BlogDetailPageSeo,
    BlogsPageSeo,
    ContactPageSeo,
    FaqPageSeo,
    HomePageSeo,
    ServiceDetailPageSeo,
    ServicesPageSeo,
)


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


@admin.register(ServiceDetailPageSeo)
class ServiceDetailPageSeoAdmin(TranslationAdmin):
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(BlogDetailPageSeo)
class BlogDetailPageSeoAdmin(TranslationAdmin):
    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }


@admin.register(HomePageSeo)
class HomepageSeoAdmin(SingletonModelAdmin):
    pass


@admin.register(ServicesPageSeo)
class ServicesPageSeoAdmin(SingletonModelAdmin):
    pass


@admin.register(AboutUsPageSeo)
class AboutUsPageSeoAdmin(SingletonModelAdmin):
    pass


@admin.register(BlogsPageSeo)
class BlogsPageSeoAdmin(SingletonModelAdmin):
    pass


@admin.register(ContactPageSeo)
class ContactPageSeoAdmin(SingletonModelAdmin):
    pass


@admin.register(AppointmentPageSeo)
class AppointmentPageSeoAdmin(SingletonModelAdmin):
    pass


@admin.register(FaqPageSeo)
class FaqPageSeoAdmin(SingletonModelAdmin):
    pass
