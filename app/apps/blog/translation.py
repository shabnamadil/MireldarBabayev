from modeltranslation.translator import TranslationOptions, register

from .models import Blog, Category, Tag


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ("title", "short_description", "content")


@register(Category)
class CategoryTranslationAdmin(TranslationOptions):
    fields = ("name",)


@register(Tag)
class TagTranslationAdmin(TranslationOptions):
    fields = ("name",)
