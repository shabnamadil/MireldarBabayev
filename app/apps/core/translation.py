from modeltranslation.translator import TranslationOptions, register

from .models import (
    AboutUs,
    Banner,
    Faq,
    SiteSettings,
    StatisticalIndicator,
    Testimoinal,
    WhoWeAre,
)


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('content', 'mission', 'vision', 'value')


@register(Banner)
class BannerTranslationAdmin(TranslationOptions):
    fields = ('title', 'subtitle', 'description')


@register(Faq)
class FaqTranslationAdmin(TranslationOptions):
    fields = ('question', 'response')


@register(SiteSettings)
class SiteSettingsTranslationAdmin(TranslationOptions):
    fields = ('location', 'footer_description')


@register(StatisticalIndicator)
class StatisticalIndicatorSettingsTranslationAdmin(TranslationOptions):
    fields = ('name',)


@register(Testimoinal)
class TestimonialTranslationAdmin(TranslationOptions):
    fields = ('client_profession', 'client_comment')


@register(WhoWeAre)
class WhoWeAreTranslationAdmin(TranslationOptions):
    fields = ('title', 'content')
