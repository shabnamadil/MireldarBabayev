from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html

from .models import CustomUser


class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    ordering = ('email', '-created_at')
    list_display = (
        'full_name',
        'email',
        'get_image',
        'is_staff',
        'is_superuser',
        'is_active',
    )
    list_filter = ('created_at',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            'Personal info',
            {'fields': ('first_name', 'last_name', 'image')},
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'user_permissions',
                    'groups',
                )
            },
        ),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'first_name',
                    'last_name',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    filter_horizontal = ('user_permissions', 'groups')
    list_per_page = 20

    def get_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:150px;height:auto;" />',
                obj.image.url,
            )
        return '-'

    get_image.short_description = "Foto"  # type: ignore


admin.site.register(CustomUser, CustomUserAdmin)
