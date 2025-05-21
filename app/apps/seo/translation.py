from modeltranslation.translator import TranslationOptions, register

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


class SeoSingletonTranslationOptions(TranslationOptions):
    fields = (
        "meta_title",
        "meta_description",
        "meta_keywords",
        "og_title",
        "og_description",
    )


class SeoDetailPageTranslationOptions(TranslationOptions):
    fields = ("meta_description", "meta_keywords", "og_description")


@register(HomePageSeo)
class HomePageSeoTranslationOptions(SeoSingletonTranslationOptions):
    pass


@register(ServicesPageSeo)
class ServicesPageSeoTranslationOptions(SeoSingletonTranslationOptions):
    pass


@register(AboutUsPageSeo)
class AboutUsPageSeoTranslationOptions(SeoSingletonTranslationOptions):
    pass


@register(BlogsPageSeo)
class BlogsPageSeoTranslationOptions(SeoSingletonTranslationOptions):
    pass


@register(ServiceDetailPageSeo)
class ServiceDetailPageSeoTranslationOptions(SeoDetailPageTranslationOptions):
    pass


@register(BlogDetailPageSeo)
class BlogDetailPageSeoTranslationOptions(SeoDetailPageTranslationOptions):
    pass


@register(ContactPageSeo)
class ContactPageSeoTranslationOptions(SeoSingletonTranslationOptions):
    pass


@register(AppointmentPageSeo)
class AppointmnetPageSeoTranslationOptions(SeoSingletonTranslationOptions):
    pass


@register(FaqPageSeo)
class FaqPageSeoTranslationOptions(SeoSingletonTranslationOptions):
    pass
