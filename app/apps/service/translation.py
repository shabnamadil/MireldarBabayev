from modeltranslation.translator import TranslationOptions, register

from .models import Coworker, Download, Service, WhyChooseUs


@register(Coworker)
class CoworkerTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Download)
class DownloadTranslationAdmin(TranslationOptions):
    fields = ('title',)


@register(Service)
class ServiceTranslationAdmin(TranslationOptions):
    fields = ('name', 'short_description', 'title', 'content')


@register(WhyChooseUs)
class WhyChooseUsTranslationAdmin(TranslationOptions):
    fields = ('title', 'short_description')
