
from modeltranslation.translator import register, TranslationOptions
from .models import (
    Blog,
    Category,
    Tag
)


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = (
        'title', 
        'short_description',
        'content'
        )
    

@register(Category)
class CategoryTranslationAdmin(TranslationOptions):
    fields = (
        'name',
    )


@register(Tag)
class TagTranslationAdmin(TranslationOptions):
    fields = (
        'name',
    )