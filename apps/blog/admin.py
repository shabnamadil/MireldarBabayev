from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from modeltranslation.admin import TranslationAdmin

from .models import (
    Category,
    Tag,
    Comment,
    Blog,
    IP
)


@admin.action(description="Mark selected items as DRAFT")
def make_draft(self, request, queryset):
    app_name = self.model._meta.app_label
    queryset.update(status=self.model.Status.DRAFT)
    self.message_user(request, f"Selected items have been marked as DRAFT in the {app_name} app.")

@admin.action(description="Mark selected items as PUBLISHED")
def make_published(self, request, queryset):
    app_name = self.model._meta.app_label
    queryset.update(status=self.model.Status.PUBLISHED)
    self.message_user(request, f"Selected items have been marked as PUBLISHED in the {app_name} app.")


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = (
        'title', 'display_blog_img',
        'display_blog_author', 'view_count',
        'display_blog_categories', 
        'show_comments_count',
        'status', 'created_date',
    )
    list_filter = (
        'created_at', 'status',
        'category', 'tag'
    )
    search_fields = (
        'title', 'content', 
        'short_description',
        'category__name',
        'tag__name'
    )
    ordering = ('-updated_at', 'title')
    date_hierarchy = 'created_at'
    list_per_page = 20
    actions =(make_draft, make_published)
    readonly_fields = (
        'author', 'slug', 
        'published_at'
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def display_blog_author(self, obj):
        author_name = obj.author.get_full_name() if obj.author.get_full_name() else 'Admin'
        url = reverse("admin:user_customuser_change", args=[obj.author.id])
        link = '<a style="color: red;" href="%s">%s</a>' % (
            url, 
            author_name
        )
        return mark_safe(link)
    display_blog_author.short_description = 'Müəllif'

    def display_blog_img(self, obj):
        image = obj.image.url
        if image:
            raw_html = f'<img style="width:70px;height:auto;" src="{image}">'
            return format_html(raw_html)
    display_blog_img.short_description = 'Cover foto'

    def display_blog_categories(self, obj):
        return ", ".join(category.name for category in obj.category.all())
    display_blog_categories.short_description = 'Kateqoriya'

    def show_comments_count(self, obj):
        result = Comment.objects.filter(blog=obj).count()
        return result
    show_comments_count.short_description = 'RƏYLƏRİN SAYI'

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'get_comment', 'display_blog',
        'display_comment_author', 
        'created_date',
    )
    list_filter = (
        'created_at',
    )
    search_fields = (
        'content',
    )
    ordering = ('-updated_at', 'content')
    date_hierarchy = 'created_at'
    list_per_page = 20
    readonly_fields = ('author',)
    autocomplete_fields = ('blog', )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def display_blog(self, obj):
        url = reverse("admin:blog_blog_change", args=[obj.blog.id])
        link = '<a style="color: blue;" href="%s">%s</a>' % (
            url, 
            obj.blog.title
        )
        return mark_safe(link)
    display_blog.short_description = 'Bloq'

    def display_comment_author(self, obj):
        url = reverse("admin:user_customuser_change", args=[obj.author.id])
        link = '<a style="color: red;" href="%s">%s</a>' % (
            url, 
            obj.author.get_full_name()
        )
        return mark_safe(link)
    display_comment_author.short_description = 'Müəllif'

    def get_comment(self, obj):
        return obj.truncated_comment
    get_comment.short_description = 'Comment'

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        if obj.author != request.user:
            return False
        return super().has_change_permission(request, obj)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', )


admin.site.register(IP)