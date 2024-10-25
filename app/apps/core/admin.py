from django.contrib import admin

from .models import Newsletter
from .models import Contact
from .forms import ContactForm


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_filter = ('created_at', )
    list_per_page = 20


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'full_name', 'email', 'phone')
    list_filter = ('created_at', )
    date_hierarchy = 'created_at'
    list_per_page = 20
    search_fields = ('full_name', 'email', 'message', 'subject')
    form = ContactForm